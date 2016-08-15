$(document).ready(function() {

  function getHashFilter() {
    var hash = location.hash;
    // get filter=filterName
    var matches = location.hash.match( /filter=([^&]+)/i );
    var hashFilter = matches && matches[1];
    return hashFilter && decodeURIComponent( hashFilter );
  }

  $( function () {
    // quick search regex
    var qsRegex;
    var buttonFilter;

    var isIsotopeInit = false;

    function onHashchange() {
      var hashFilter = getHashFilter();
      if ( !hashFilter && isIsotopeInit ) {
        return;
      }
      isIsotopeInit = true;
      // init Isotope
      var $container = $('section.apps > ul').isotope({
        itemSelector: 'section.apps > ul > li',
        layoutMode: 'fitRows',
        filter: hashFilter,
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

        // set filter in hash
        if ( buttonFilter ) {
          hashValue = buttonFilter.replace('.selector-', '');
        }
        else {
          hashValue = '';
        }
        location.hash = encodeURIComponent( hashValue );
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

          //active classes for overviews
          $('.overviews').find('.overview.active').removeClass('active');
          $('.overviews').find($(this).data("pid")).addClass('active');

        });
      });
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
