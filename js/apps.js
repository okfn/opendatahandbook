$(document).ready(function() {

  function getHashFilter() {
    var hash = location.hash;
    // get filter=filterName
    var matches = location.hash.match( /filter=([^&]+)/i );
    var hashFilter = matches && matches[1];
    return hashFilter && decodeURIComponent( hashFilter );
  }

  $( function() {

    var $container = $('section.apps > ul');
    var qsRegex;

    // bind filter button click
    var $filters = $('.filter').on( 'click', 'a', function() {
      var filterAttr = $( this ).attr('data-filter');
      // set filter in hash
      if ( filterAttr ) {
        hashValue = filterAttr;
      }
      else {
        hashValue = '*';
      }
      location.hash = 'filter=' + encodeURIComponent( hashValue );

      //active classes for overviews
      $('.overviews').find('.overview.active').removeClass('active');
      $('.overviews').find($(this).data("pid")).addClass('active');
    });

    // use value of search field to filter
    var $quicksearch = $('.quicksearch').keyup( debounce( function() {
      qsRegex = new RegExp( $quicksearch.val(), 'gi' );
      $container.isotope();
    }) );

    var isIsotopeInit = false;

    function onHashchange() {
      var hashFilter = getHashFilter();
      if ( !hashFilter && isIsotopeInit ) {
        return;
      }

      isIsotopeInit = true;
      // filter isotope
      $container.isotope({
        itemSelector: 'section.apps > ul > li',
        layoutMode: 'fitRows',
        filter: function() {
          var $this = $(this);
          var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
          var hashResult = hashFilter ? $this.is( hashFilter ) : true;
          return searchResult && hashResult;
        }
      });
      // set selected class on button
      if ( hashFilter ) {
        $filters.find('.active').removeClass('active');
        $filters.find('[data-filter="' + hashFilter + '"]').addClass('active');
      }
    }

    $(window).on( 'hashchange', onHashchange );
    // trigger event handler to init Isotope
    onHashchange();
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
