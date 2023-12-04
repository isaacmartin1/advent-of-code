const fs = require("fs")

let lines = fs.readFileSync("real.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function main(lines) {
    console.log(lines)
    let parsedLines = parseLines(lines)
    console.log(parsedLines)
    let answer = getScore(parsedLines)
    console.log(answer)
}

function parseLines(lines) {
    let parsedLines = []
    for (let i = 0; i<lines.length; i++) {
        parsedLines.push(lines[i].split(/:|\|/))
    }
    return parsedLines
}

function getScore(parsedLines) {
    let totalPoints = 0
    for (let x=0; x<parsedLines.length; x++) {
        possibleScores = parseOnSpaces(parsedLines[x][1])
        // console.log(possibleScores)
        numbersOnCard = parseOnSpaces(parsedLines[x][2])
        // console.log(numbersOnCard)
        totalPointsPerLine = matchScores(possibleScores, numbersOnCard)
        console.log(totalPointsPerLine)
        totalPoints += totalPointsPerLine
    }
    return totalPoints
}

function parseOnSpaces(inputString) {
    const validArray = []
    let candidateArray = inputString.split(/ /)
    for (u=0; u<candidateArray.length; u++) {
        if (candidateArray[u].length > 0) {
            validArray.push(candidateArray[u])
        }
    }
    return validArray
}

function matchScores(possibleScores, numbersOnCard) {
    let totalPointsPerLine = 0
    // use possible scores because its shorter
    for (let r=0; r<possibleScores.length; r++) {
        if (numbersOnCard.includes(possibleScores[r])) {
            totalPointsPerLine= fibonnaciScore(totalPointsPerLine)
        }
    }
    return totalPointsPerLine
}

function fibonnaciScore(totalPointsPerLine) {
    if (totalPointsPerLine === 0) {
        return totalPointsPerLine = 1
    } else {
        return totalPointsPerLine *= 2
    }
}


masterNumber = main(lines)