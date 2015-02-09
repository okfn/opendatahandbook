$(document).ready(function() {
    $("#menu").mmenu({
        classes: "mm-light"
     });
     
     
     var inview = new Waypoint.Inview({
        element: $('.site-footer')[0],
        enter: function() {
          $( "body" ).addClass( "footer-in-view" );
        },
        
        exited: function() {
          $( "body" ).removeClass( "footer-in-view" );
        },
        
      })
 });