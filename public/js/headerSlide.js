// Funktion für den HeaderSloganSlider

$(function(){

    // Funktion für HeaderSlider

    let container = $("#slideAnimation");
    let firstchildren = $("#slideAnimation li:first");
    let countFlag = 0;
    setInterval(function(){
        container.children().removeClass('active');



    },5000);


    // Karten sind immer gleich groß
    let form = $(".choose-profit");
    var count = 0;
    form.children().each(function(){
        let test = $(this).outerWidth();
        if(test > count){
            count = test;
        }
    });
    form.children('input').css({"width": count});
    $('input').css({"width": count});
    // Events

    var percentage = $("#percent");
    var discount = $("#discount");
    var children = form.children();
    var newCardInfo = $(".new-card-info");
    form.children("input").each(function(){
        $(this).on("click touch", function(){
            children.hide();
            newCardInfo.show();

        });
    });


})
