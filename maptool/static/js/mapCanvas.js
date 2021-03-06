var actual_id = "cabin"
var img;

function addToCanvas(clicked_id) {

    var canvas = document.getElementById("myCanvas");
    var context = canvas.getContext("2d");
    context.clearRect(0, 0, canvas.width, canvas.height);
    self.actual_id = clicked_id;
    self.img = document.getElementById(self.actual_id);
    context.drawImage(this.img,0,0);
}

function draw(scale, translatePos){
    var canvas = document.getElementById("myCanvas");
    var context = canvas.getContext("2d");
    

    // clear canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    context.save();
    context.translate(translatePos.x, translatePos.y);
    context.scale(scale, scale);
    self.img = document.getElementById(self.actual_id);
    context.drawImage(self.img,0,0);
    context.restore();
}

window.onload = function(){
    var canvas = document.getElementById("myCanvas");

    var translatePos = {
        x: canvas.width / 2,
        y: canvas.height / 2
    };

    var scale = 1.0;
    var scaleMultiplier = 0.8;
    var startDragOffset = {};
    var mouseDown = false;

    // add button event listeners
    document.getElementById("plus").addEventListener("click", function(){
        scale /= scaleMultiplier;
        draw(scale, translatePos);
    }, false);

    document.getElementById("minus").addEventListener("click", function(){
        scale *= scaleMultiplier;
        draw(scale, translatePos);
    }, false);

    // add event listeners to handle screen drag
    canvas.addEventListener("mousedown", function(evt){
        mouseDown = true;
        startDragOffset.x = evt.clientX - translatePos.x;
        startDragOffset.y = evt.clientY - translatePos.y;
    });

    canvas.addEventListener("mouseup", function(evt){
        mouseDown = false;
    });

    canvas.addEventListener("mouseover", function(evt){
        mouseDown = false;
    });

    canvas.addEventListener("mouseout", function(evt){
        mouseDown = false;
    });

    canvas.addEventListener("mousemove", function(evt){
        if (mouseDown) {
            translatePos.x = evt.clientX - startDragOffset.x;
            translatePos.y = evt.clientY - startDragOffset.y;
            draw(scale, translatePos);
        }
    });

    draw(scale, translatePos);
};



jQuery(document).ready(function(){
    $("#wrapper").mouseover(function(e){
        $('#status').html(e.pageX +', '+ e.pageY);
    }); 
})  