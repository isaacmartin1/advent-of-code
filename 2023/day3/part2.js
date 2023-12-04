const fs = require("fs")

let lines = fs.readFileSync("input.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function main(lines) {
    console.log(lines[lines.length-1])
    let allNumbers = []
    let lineNumbers
    let allAsterisks = []
    let lineAsterisks
    for (i = 0; i < lines.length; i++) {
        lineNumbers = collectNumbers(lines[i])
        allNumbers.push(lineNumbers)
    }
    console.log(allNumbers)


    for (m=0; m< lines.length; m++) {
        lineAsterisks = collectAsterisks(lines[m])
        allAsterisks.push(lineAsterisks)
    }
    console.log(allAsterisks)

    let masterNumber = evaluateAsteriskArray(allAsterisks, allNumbers)

    console.log(masterNumber)
}


// search all the numbers
// add them all together
// subtract for each one that doesn't have a symbol near it
// this avoids repeats


function collectNumbers(line) {
    let numberString = ''
    let numberArray=[]
    let tempPositionArray = []
    for (x=0; x < line.length; x++) {
        if (/^[0-9]*$/.test(line[x]) === true) {
            numberString += line[x]
            tempPositionArray.push(x)
            if (x === line.length-1) {
                numberArray.push([Number(numberString), tempPositionArray])
                return numberArray
            }
        } else {
            if (tempPositionArray.length > 0 && numberString.length > 0) {
                numberArray.push([Number(numberString), tempPositionArray])
                tempPositionArray = []
                numberString = ''
            }
        }
    }
    return numberArray
}

function collectAsterisks(line) {
    let asteriskArray=[]
    for (x=0; x < line.length; x++) {
        if (/[*]/.test(line[x]) === true) {
            asteriskArray.push(x)
        }
    }
    return asteriskArray
}

function evaluateAsteriskArray(allAsterisks, allNumbers) {
    let masterNumberFn = 0
    for (let t=0; t<allAsterisks.length; t++) {
        // for every asterisk, check the numbers array above, on the level, and below for matches
        // two number matches means the numbers found will be multiplied together and added to masterNumberFn
        // find matches on row above
        // allNumbers[t-1]
        // find matches on row
        // allNumbers[t]
        // find matches on row below
        // allNumbers[t+1]
        for (let n=0; n<allAsterisks[t].length; n++) {
            // console.log(allAsterisks[t][n])
            for (let c = t-1; c<=t+1; c++) {
                let totalNumberFound = 0
                let contenderNumber = 0
                for (let b=0; b<allNumbers[c].length; b++) {
                    // allNumbers[c][b] is the individual number being evaluated here
                    // console.log(allNumbers[c][b])
                    let foundMatch = false
                    for (let a=0; a<allNumbers[c][b][1].length; a++) {
                        if (foundMatch === true) {break}
                        if (allAsterisks[t][n] === allNumbers[c][b][1][a] || allAsterisks[t][n]+1 === allNumbers[c][b][1][a] || allAsterisks[t][n]-1 === allNumbers[c][b][1][a]) {
                            // console.log(allNumbers[c][b][1][a])
                            foundMatch = true
                        }
                    }
                    if (foundMatch === true) {
                        totalNumberFound += 1
                        if (totalNumberFound === 1) {
                            // add actual value
                            contenderNumber += allNumbers[c][b][0]
                        } else if (totalNumberFound === 2) {
                            // multiply it in
                            contenderNumber = contenderNumber * allNumbers[c][b][0]
                        } else {
                            contenderNumber = 0
                            totalNumberFound = 0
                            break
                        }
                    }
                    foundMatch = false
                }
                if (totalNumberFound === 2) {
                    console.log(contenderNumber)
                    masterNumberFn += contenderNumber
                    // console.log(masterNumberFn)
                    totalNumberFound = 0
                    contenderNumber = 0
                }
            }

        }
    }
    return masterNumberFn

}


masterNumber = main(lines)