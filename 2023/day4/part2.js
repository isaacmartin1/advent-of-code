const fs = require("fs")

let lines = fs.readFileSync("real.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function main(lines) {
    let parsedLines = parseLines(lines)
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
    let pointArray = []
    for (let x=0; x<parsedLines.length; x++) {
        possibleScores = parseOnSpaces(parsedLines[x][1])
        numbersOnCard = parseOnSpaces(parsedLines[x][2])
        matchesFound = matchScores(possibleScores, numbersOnCard)
        pointArray.push(matchesFound)
    }
    let totalPoints = parseScoreFromMatches(pointArray)
    return totalPoints
}

function parseScoreFromMatches(pointArray) {
    numOfMatches = transformPointArray(pointArray)
    console.log(numOfMatches)
    let sumOfCards = 0
    for (let g=0; g<numOfMatches.length; g++) {
        sumOfCards += numOfMatches[g]
    }
    return sumOfCards
}

function transformPointArray(pointArray) {
    numOfCopies = []
    for (let n = 0; n<pointArray.length; n++) {
        numOfCopies.push(1)
    }

    for (let i = 0; i< pointArray.length; i++) {
        for (let j=1; j<=pointArray[i]; j++) {
            numOfCopies[i+j] = numOfCopies[i+j] + (numOfCopies[i])
        }
    }
    return numOfCopies
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
    let matchesFound = 0
    // use possible scores because its shorter
    for (let r=0; r<possibleScores.length; r++) {
        if (numbersOnCard.includes(possibleScores[r])) {
            matchesFound++
        }
    }
    return matchesFound
}

masterNumber = main(lines)