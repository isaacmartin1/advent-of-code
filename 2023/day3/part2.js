const fs = require("fs")

let lines = fs.readFileSync("real.csv", {encoding: "utf-8"}).split("\n")

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
        for (let n=0; n<allAsterisks[t].length; n++) {
            let totalNumberFound = 0
            let contenderNumber = 0
            for (let c = t-1; c<=t+1; c++) {
                let foundMatch = false
                // loop each row above, on, below
                for (let b=0; b<allNumbers[c].length; b++) {
                    // allNumbers[c][b] is the individual number being evaluated here
                    for (let a=0; a<allNumbers[c][b][1].length; a++) {
                        if (foundMatch === true) {break}
                        if (allAsterisks[t][n] === allNumbers[c][b][1][a] || allAsterisks[t][n]+1 === allNumbers[c][b][1][a] || allAsterisks[t][n]-1 === allNumbers[c][b][1][a]) {
                            foundMatch = true
                        }
                    }
                    if (foundMatch === true) {
                        totalNumberFound += 1
                        if (totalNumberFound === 1) {
                            contenderNumber += allNumbers[c][b][0]
                            console.log(contenderNumber)
                        } else if (totalNumberFound === 2) {
                            contenderNumber = contenderNumber * allNumbers[c][b][0]
                            console.log(contenderNumber)
                        } else {
                            contenderNumber = 0
                            break
                        }
                    }
                    foundMatch = false
                }
            }
            if (totalNumberFound === 2) {
                masterNumberFn += contenderNumber
                totalNumberFound = 0
                contenderNumber = 0
                foundMatch = false
            }
        }
    }
    return masterNumberFn

}

masterNumber = main(lines)