
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
            
            tocParams = {
                
                'selectors': 'h1,h2,h3', //elements to use as headings
                'container': 'body', //element to find all selectors in
                'smoothScrolling': true, //enable or disable smooth scrolling on click
                 //doesn't work  'prefix': 'algolab-toc', //prefix for anchor tags and class names
                //'onHighlight': function(el) {}, //called when a new section is highlighted 
                'highlightOnScroll': true, //add class to heading that is currently in focus
                'highlightOffset': 100, //offset to trigger the next headline
                'anchorName': function(i, heading, prefix) { //custom function for anchor name
                    return prefix+i;
                },
                'headerText': function(i, heading, $heading) { //custom function building the header-item text
                    console.log("$heading.text()=",$heading.text());
                    return $heading.text().replace("¶","");
                },
                'itemClass': function(i, heading, $heading, prefix) { // custom function for item class
                return $heading[0].tagName.toLowerCase();
                }                
            }
            
            $('#algolab-toc').toc(tocParams);
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
