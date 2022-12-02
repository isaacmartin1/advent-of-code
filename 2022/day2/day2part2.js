const fs = require("fs")

let lines = fs.readFileSync("day2.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

let scoreFromChoice = 0
let scoreFromResult = 0

for (let i=0; i<lines.length; i++) {
    if (lines[i][2] === 'X') {
        scoreFromResult += 0
    }
    if (lines[i][2] === 'Y') {
        scoreFromResult += 3
    }
    if (lines[i][2] === 'Z') {
        scoreFromResult += 6
    }

    // a = rock
    // b = paper
    // c = scissors

    // x = lose
    // y = draw
    // z = win

    const rock = 1
    const paper = 2
    const scissors = 3
    if (lines[i][0] === 'A' && lines[i][2] === 'X') {
            scoreFromChoice += scissors
    }
    if (lines[i][0] === 'B' && lines[i][2] === 'Y') {
            scoreFromChoice += paper
    }
    if (lines[i][0] === 'C' && lines[i][2] === 'Z') {
            scoreFromChoice += rock
    }
    if (lines[i][0] === 'A' && lines[i][2] === 'Y') {
            scoreFromChoice += rock
    }
    if (lines[i][0] === 'B' && lines[i][2] === 'Z') {
            scoreFromChoice += scissors
    }
    if (lines[i][0] === 'C' && lines[i][2] === 'X') {
            scoreFromChoice += paper
    }
    if (lines[i][0] === 'A' && lines[i][2] === 'Z') {
        scoreFromChoice += paper
    }
    if (lines[i][0] === 'B' && lines[i][2] === 'X') {
            scoreFromChoice += rock
    }
    if (lines[i][0] === 'C' && lines[i][2] === 'Y') {
            scoreFromChoice += scissors
    }
}

console.log(scoreFromChoice+scoreFromResult)