var canva;
var ctx;
// C'est pas bien d'initialiser à des valeurs au pif
var minX = 0;
var minY = 0;
var maxX = 0;
var maxY = 0;
var dX = 0;
var dY = 0;

function loadCanva() {
    canva = document.getElementById("canva");
    ctx = canva.getContext("2d");
}

function loadFile() {
    $.get("tact.txt", function(response) {
        var data = response.split("\n");

        for(var i = 0; i < data.length; i++) {
            data[i] = data[i].split(' ')
        }

        var positions = [];

        for(var t = 0; t < data[0].length; t++) {
            var positionsT = [];
            for(var i = 0; i < 36; i++) {
                var x =  data[i*2][t];
                var y =  data[i*2+1][t];

                minX = Math.min(x, minX)
                minY = Math.min(y, minY)
                maxX = Math.max(x, maxX)
                maxY = Math.max(y, maxY)

                var collegien = [
                    x, // x
                    y // y
                ]
                positionsT.push(collegien)
            }
            positions.push(positionsT)
        }

        console.log("minX", minX, "minY", minY, "maxX", maxX, "maxY", maxY);
        dX = maxX - minX;
        dY = maxY - minY;
        console.log('Plot started')
        plotPos(positions);
    });
}

function plotPos(positions) {
    if(positions.length == 0) {
        return;
    }

    console.log("Positions restantes : " + positions.length)

    var positionsT = positions.shift();

    ctx.clearRect(0, 0, canva.width, canva.height);

    for(var i = 0; i < positionsT.length; i++) {
        var collegien = positionsT[i]

        var x = collegien[0];
        var y = collegien[1];

        x = (x - minX)/dX*canva.width;
        y = (y - minY)/dY*canva.height;

        ctx.fillRect(x,y,1,1);
    }

    setTimeout(function() {
        plotPos(positions)
    }, 1);
}

loadCanva();
loadFile();