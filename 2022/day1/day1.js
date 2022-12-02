const fs = require("fs")

let lines = fs.readFileSync("day1input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

console.log(lines)

let currentElfTotal = 0;
let elfList = []

for (let i=0; i<lines.length; i++) {
    if (lines[i].length === 0) {
        elfList.push(currentElfTotal)
        currentElfTotal = 0
    } else {
        currentElfTotal += Number(lines[i])
    }
}

console.log(elfList)

numberSort = function(a,b) {
    return b-a;
}

console.log(elfList.sort(numberSort))