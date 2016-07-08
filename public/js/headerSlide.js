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
    $('input').css({"width": count});

    // Events
    //app
    var app = $(".card-preview");
    //app childs
    var percentage = $("#percent");
    var discount = $("#discount");
    var children = form.children();
    var newCardInfo = $(".new-card-info");
    var moreInfos = $(".moreInfos");
    var returnPage = $("#return");
    // startbutton
    var initBtn = $(".double-bounce");

    form.children("input").each(function(){
        $(this).on("click touch", function(){
            children.hide();
            newCardInfo.show();
            newCardInfo.children().each(function(){
                // wenn percent oder coins geklickt wurde wird beide
                // male der gleich view aufgerufen
                $(this).on("click touch", function(){
                    newCardInfo.children().hide();
                    let that = $(this).attr("name");
                    if(that == "newCard"){
                        // wenn new card geklickt wurde
                            initBtn.on("click touch", function(){
                                app.show();
                            });
                    }
                    if(that == "moreInfos"){
                        // wenn auf more infos geklickt wurde
                        moreInfos.show();
                        moreInfos.children().each(function(){
                            $(this).on("click touch", function(){
                                if($(this).attr('value')){
                                    app.hide();
                                }
                            });

                        });
                    }
                });
            });

        });
    });




});
