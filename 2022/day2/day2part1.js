const fs = require("fs")

let lines = fs.readFileSync("day2.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

let scoreFromChoice = 0
let scoreFromResult = 0
for (let i=0; i<lines.length; i++) {
    // score from choice
    if (lines[i][2] === 'X') {
        scoreFromChoice += 1
    } else if (lines[i][2] === 'Y') {
        scoreFromChoice += 2
    } else if (lines[i][2] === 'Z') {
        scoreFromChoice += 3
    }
    
    // tie
    if (lines[i][0] === 'A' && lines[i][2] === 'X') {
            scoreFromResult += 3
    }

    if (lines[i][0] === 'B' && lines[i][2] === 'Y') {
            scoreFromResult += 3
    }

    console.log(lines[i][0], lines[i][2])
    if (lines[i][0] === 'C' && lines[i][2] === 'Z') {
            scoreFromResult += 3
    }

    // win
    if (lines[i][0] === 'A' && lines[i][2] === 'Y') {
            scoreFromResult += 6
    }
    if (lines[i][0] === 'B' && lines[i][2] === 'Z') {
            scoreFromResult += 6
    }

    if (lines[i][0] === 'C' && lines[i][2] === 'X') {
            scoreFromResult += 6
    }
}

console.log(scoreFromChoice+scoreFromResult)