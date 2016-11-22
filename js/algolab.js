
function showthis(url) {
    window.open(url, "pres", "toolbar=yes,scrollbars=yes,resizable=yes,top=10,left=400,width=500,height=500");
    return(false);
}

var algolab = {
    
    isReduced : function(){
        return $(window).width() < 924;
    },
    hoverToc : function(){
        return $('#algolab-toc:hover').length != 0;
    },
    resize : function(){
        if (algolab.isReduced()){
            $("#algolab-toc").hide();
        } else {
            $("#algolab-toc").show();
            $("#algolab-toc").css("background","rgba(255, 255, 255, 0)");
        }
    },
    init : function(){
       algolab.hideCellStartingWith("%%HTML");
       algolab.hideCellStartingWith("import algolab");
       algolab.hideCellStartingWith("algolab.init()");
       algolab.resize();
    }, 
    hideCellStartingWith : function(text){
        $('.border-box-sizing .code_cell pre').filter(function() { 
                return $(this).text().indexOf(text) === 0; 
            }).parents('div .cell').hide();        
    }
}

$( window ).resize(function() {
    console.log("Resizing window !");
    algolab.resize();
});


$("body").on("mousemove",function(event) {
    if (algolab.isReduced()){
        if (event.pageX < 50) {            
             $("#algolab-toc").show(); 
            $("#algolab-toc").css("background","rgba(255, 255, 255, 1.0)");
        } else {
            
            if (algolab.hoverToc()) {                    
            } else {
                $("#algolab-toc").hide();                        
            }
                     
/*            if ($("#algolab-toc").is(":visible")){
                if (algolab.hoverToc()) {                    
                } else {
                    $("#algolab-toc").hide();                        
                }
            } else {
                if (algolab.hoverToc())
                  show
              } else {
                $("#algolab-toc").hide();                        
               }                 
            }
  */     
        }
    }
});

$(document).ready(algolab.init);
