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
      
    // external links in new window
    var extAnchors = $('a[rel~=external]');
    $.each(
        extAnchors,
        function (index, item) {
            $(item).attr('target', '_blank');
        }
    );
    
    
    //dropdown
    $(".dropdown-button").click(function() {
      $(".dropdown-menu").toggleClass("show-menu");
      $(".dropdown-menu > li").click(function(){
        $(".dropdown-menu").removeClass("show-menu");
      });
      
    });
    
    
    //filters
    $("#menu .filter > a").click(function() { 
      $(this).parent('.filter').toggleClass("active");
    });    
    
    //resources
    $(".resources .results .icon-info").click(function() { 
      $(this).parent('aside').toggleClass("active");
    }); 
 });