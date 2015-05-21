$(document).ready(function() {
    $("#menu .filter .filter-items > a").click(function() { 
        $("#menu .filter .filter-items > a").removeClass("active");  
        $(this).toggleClass("active");
        filter_type = $(this).attr("data-filter");
        filter_value = $(this).attr("data-value");
        test = 0;
        $("ul.results > li").each(function(index, value) {
             type = $(this).find("dd." + filter_type).first()
             if(type.length && type.text() == filter_value){
                 $(this).show("slow");
             } else {
                 $(this).hide("slow");
             }
        });
        $("div.resources > section.topics").hide("slow");
        $("div.resources > section.media-types").hide("slow");
    });  
    
    // toggle info
    $(".resources .results .icon-info").click(function() { 
      $(this).parent('aside').toggleClass("active");
    });   
});
