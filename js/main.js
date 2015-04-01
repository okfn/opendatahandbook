$(document).ready(function() {
    // Menu
    $("#menu").mmenu({
        classes: "mm-light"
     });
     
     // Detect if scrolled to footer
     var inview = new Waypoint.Inview({
        element: $('.site-footer')[0],
        enter: function() {
          $( "body" ).addClass( "footer-in-view" );
        },
        exited: function() {
          $( "body" ).removeClass( "footer-in-view" );
        },
      })
      
      // Append headings with link to ID
      function headingLink(heading) {
        $.each($(heading), function() {
          var headingID = $(this).attr('id');
          var headingURL = '#' + headingID;
          if(typeof headingID != 'undefined') {
            $( this ).append( '<a class="headerlink" href="'+headingURL+'" title="Permalink to this heading"><span class="icon-section"></span></a>' );
          }
        });
      }
      headingLink('h3');
      headingLink('h4');
 });