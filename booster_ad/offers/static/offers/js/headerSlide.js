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
    var form = $(".choose-profit");
    // var count = 0;
    // form.children().each(function(){
    //     let test = $(this).outerWidth();
    //     if(test > count){
    //         count = test;
    //     }
    // });
    // form.children().css({"width": count});
    // $('input').css({"width": count});

    // Events

    //variables
    var cardPreview = $(".card-preview");
    //app childs
    var percentage = $("#percent");
    var discount = $("#discount");
    var children = form.children();
    var newCardInfo = $(".new-card-info");
    var moreInfos = $(".moreInfos");
    var returnPage = $("#return");
    var bounceCircle = $(".double-bounce");
    // startbutton
    var initBtn = $("#eventTicker");
    //blackcards
    var blackCardsContainer = $(".black-cards");

    //app
    function app(){
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
                            $(document).css({"background-color": "white"});
                            window.location.reload();
                        }
                        if(that == "moreInfos"){
                            // wenn auf more infos geklickt wurde
                            moreInfos.show();
                            moreInfos.children().each(function(){
                                $(this).on("click touch", function(){
                                    if($(this).attr('value')){
                                        cardPreview.hide();
                                        window.location.reload();
                                    }
                                });

                            });
                        }
                    });
                });

            });
        });

    }
    // click on the circlebtn
    initBtn.on("click touch", function(){
        bounceCircle.css({"display": "none"});
        renderBlackcard();
    });
    // render  blackcards + animate/hide
    function renderBlackcard(){
        blackCardsContainer.show();
        blackCardsContainer.children().each(function(){
            $(this).on("click touch", function(){
                blackCardsContainer.hide();
                cardPreview.show();
                app();
            });
        });
    }



});
