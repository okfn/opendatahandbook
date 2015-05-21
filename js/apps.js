$(document).ready(function() {
   $( function() {
    // quick search regex
    var qsRegex;
    var buttonFilter;
    
    // init Isotope
    var $container = $('section.apps > ul').isotope({
      itemSelector: 'section.apps > ul > li',
      layoutMode: 'fitRows',
      filter: function() {
        var $this = $(this);
        var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
        var buttonResult = buttonFilter ? $this.is( buttonFilter ) : true;
        return searchResult && buttonResult;
      }
    });
  
    $('.filter').on( 'click', 'a', function() {
      buttonFilter = $( this ).attr('data-filter');
      $container.isotope();
    });
    
    // use value of search field to filter
    var $quicksearch = $('.quicksearch').keyup( debounce( function() {
      qsRegex = new RegExp( $quicksearch.val(), 'gi' );
      $container.isotope();
    }) );
  
    
      // change is-checked class on buttons
    $('.filter').each( function( i, buttonGroup ) {
      var $buttonGroup = $( buttonGroup );
      $buttonGroup.on( 'click', 'a', function() {
        $('.app-sub-menu').find('.filter-items .active').removeClass('active');
        $( this ).addClass('active');
      });
    });
    
    
  });
  
  // debounce so filtering doesn't happen every millisecond
  function debounce( fn, threshold ) {
    var timeout;
    return function debounced() {
      if ( timeout ) {
        clearTimeout( timeout );
      }
      function delayed() {
        fn();
        timeout = null;
      }
      setTimeout( delayed, threshold || 100 );
    };
  }
 });