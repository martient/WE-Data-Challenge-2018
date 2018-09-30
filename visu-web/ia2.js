var canva;
var ctx;
var width;
var height;
var it;

var TEMPS = 1;
var ECHELLE = 1;
var DEBUT = 0;

var prenoms = [
"Andréa",
"Baptiste",
"Léa",
"Damien",
"Eddy",
"Flo",
"Guy",
"Henry",
"Yoann",
"Astrid",
"Will",
"Anne",
"Johan",
"Kevin",
"Louise",
"Max",
"Noa",
"Olaf",
"Patrick",
"Quentin",
"Alix",
"Benoit",
"Catia",
"Hugo",
"Andy",
"Arnaud",
"Robert",
"Ivan",
"Sophie",
"Tibo",
"Ulrick",
"Véro",
"Xavier",
"Zoe",
"Lyderic",
"Julie",
]

function loadCanva() {
    it = document.getElementById("it");
    canva = document.getElementById("canva");
    width = canva.width-10
    height = canva.height-10
    ctx = canva.getContext("2d");
    ctx.font = "10px Arial";
}

function loadFile() {
    $.get("tact.txt", function(response) {
        var data = response.split("\n");

        for(var i = 0; i < data.length; i++) {
            data[i] = data[i].split(' ')
        }

        var positions = [];

        for(var t = DEBUT; t < data[0].length; t++) {
            var positionsT = [];
            for(var i = 0; i < 36; i++) {
                var x =  data[i*2][t];
                var y =  data[i*2+1][t];

                var collegien = [ x,y ]
                positionsT.push(collegien)
            }
            positions.push(positionsT)
        }

        console.log('Plot started')

        plotPos(positions);
    });
}

function plotPos(positions) {
    if(positions.length == 0) {
        return;
    }

    it.innerHTML = positions.length
    var positionsT = positions.shift();

    ctx.clearRect(0, 0, canva.width, canva.height);


    // C'est pas bien d'initialiser à des valeurs au pif
    var minX = positionsT[0][0];
    var minY = positionsT[0][1];
    var maxX = positionsT[0][0];
    var maxY = positionsT[0][1];

    for(var i = 1; i < positionsT.length; i++) {
        var x =  positionsT[i][0];
        var y =  positionsT[i][1];

        minX = Math.min(x, minX)
        minY = Math.min(y, minY)
        maxX = Math.max(x, maxX)
        maxY = Math.max(y, maxY)
    }

    minX -= 1;
    minY -= 1;
    maxX += 1;
    maxY += 1;

    var dX = maxX - minX;
    var dY = maxY - minY;
    
    for(var i = 0; i < positionsT.length; i++) {
        var collegien = positionsT[i]

        var x = collegien[0];
        var y = collegien[1];

        x = (x - minX)/dX*width;
        y = (y - minY)/dY*height;

        ctx.fillRect(x+5,y+5,5,5);
        ctx.fillText(prenoms[i],x+3,y+3);
        ctx.fillStyle="red"
        ctx.fillRect(5,5,ECHELLE/dX*width,ECHELLE/dY*height);
        ctx.fillStyle="black"
    }

    setTimeout(function() {
        plotPos(positions)
    }, TEMPS);
}

loadCanva();
loadFile();