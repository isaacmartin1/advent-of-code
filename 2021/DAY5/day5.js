const { arrayBuffer } = require("stream/consumers")

fs = require("fs")
let lines = fs. readFileSync("day5.txt", {encoding: "utf-8"}).split("\n")

// split lines by arrow
splitLines = []
for (let x = 0; x < lines.length; x++) {
    splitLines.push(lines[x].split(" -> "))
}

// split lines by comma
lines = []
for (let x = 0; x < splitLines.length; x++) {
    lines.push([splitLines[x][0].split(","),
    splitLines[x][1].split(",")])
}

// change values to numeric while maintaining nested structure
for (let i = 0; i < lines.length; i++) {
    for (let x = 0; x < lines[0].length; x++) {
        for (let u = 0; u < lines[0][0].length; u++) {
            lines[i][x][u] = parseInt(lines[i][x][u])
        }
    }
}

xCoords = []
yCoords = []

for (let i = 0; i < lines.length; i++) {
    for (let x = 0; x < 2; x++) {
        xCoords.push(lines[i][x][0]);
        yCoords.push(lines[i][x][1]);
    }
}
console.log(Math.max.apply(null, xCoords), Math.max.apply(null, yCoords),
Math.min.apply(null, xCoords), Math.min.apply(null, yCoords))

// create map
let oneDimensionalMap = []
for (let x = 0; x < 1000; x++) {
    oneDimensionalMap.push(0)
}

let map = []
for (let x = 0; x < 1000; x++) {
    map.push(oneDimensionalMap)
}
console.log(map)
function dangerousCoordinates(lines) {
    for (let i = 0; i < lines.length; i++) {
        let x1 = lines[i][0][0];
        let x2 = lines[i][1][0];
        let y1 = lines[i][0][1];
        let y2 = lines[i][1][1];
        if (x1 === x2) { // x coords match
            for (let difference = 0; 
                difference < Math.abs(y1 - y2);
                difference++) {
                    console.log(x1, y1+difference)
                    map[x1][y1+difference] += 1;
                }
        }
        else if (y1 === y2) { // y coords match
            for (let difference = 0; 
                difference < Math.abs(x1 - x2);
                difference++) {
                    map[x1+difference][y1] += 1;
                }
        }
    }
}
dangerousCoordinates(lines);

let total = 0;
for (let x = 0; x < 1000; x++) {
    for (let y = 0; y < 1000; y++) {
        if (map[x][y] >= 2) {
            total +=1;
        }
    }
}
console.log(map)