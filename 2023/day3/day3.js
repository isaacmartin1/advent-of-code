const fs = require("fs")

let lines = fs.readFileSync("real.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function main(lines) {
    console.log(lines[lines.length-1])
    let allNumbers = []
    let lineNumbers
    for (i = 0; i < lines.length; i++) {
        lineNumbers = collectNumbers(lines[i])
        allNumbers.push(lineNumbers)
    }
    console.log(allNumbers)

    let masterNumber = validateResults(allNumbers, lines)
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
        console.log(line[x])
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

function validateResults(numberArray, lines) {
    // loop through each line
    let masterNumber = 0
    for (u=0; u<numberArray.length; u++) {
        if (numberArray.length === 0) {continue}
        // loop through each individual number's array
        for (let v=0; v<numberArray[u].length; v++) {
            // check line minesweeper everything surrounding
            // loop through each x coordinate
            let foundSpecialChar = false
            let currentTargetNumber = numberArray[u][v][0]
            for (z=0; z<numberArray[u][v][1].length; z++) {
                x_coordinate = numberArray[u][v][1][z]
                y_coordinate = u
                // mine sweeper around to find a special character, return true if found
                console.log('--------------')
                console.log('start of', currentTargetNumber, 'iteration', z)
                preliminaryResult = validateSurroundings(x_coordinate, y_coordinate, lines)
                if (preliminaryResult === true) { foundSpecialChar = true }
            }
            // if found, add to master
            if (foundSpecialChar === true) {
                console.log('added', currentTargetNumber)
                masterNumber += currentTargetNumber
            } else {
                console.log('did not add', currentTargetNumber)
            }

        }
    }
    return masterNumber
}

function validateSurroundings(x_coord, y_coord, lines) {
    if (y_coord-1 > 0) {
        if (/[^0-9.]/.test(lines[y_coord-1][x_coord-1]) === true && lines[y_coord-1][x_coord-1] !== undefined) { return true }
        if (/[^0-9.]/.test(lines[y_coord-1][x_coord+1]) === true && lines[y_coord-1][x_coord+1] !== undefined) { return true }
        if (/[^0-9.]/.test(lines[y_coord-1][x_coord]) === true && lines[y_coord-1][x_coord] !== undefined) { return true }
    }
    if (y_coord+1 <= lines.length-1) {
        if (/[^0-9.]/.test(lines[y_coord+1][x_coord+1]) === true && lines[y_coord+1][x_coord+1] !== undefined) { return true }
        if (/[^0-9.]/.test(lines[y_coord+1][x_coord]) === true && lines[y_coord+1][x_coord] !== undefined) { return true }
        if (/[^0-9.]/.test(lines[y_coord+1][x_coord-1]) === true && lines[y_coord+1][x_coord-1] !== undefined) { return true }
    }
    if (/[^0-9.]/.test(lines[y_coord][x_coord-1]) === true && lines[y_coord][x_coord-1] !== undefined) { return true }
    if (/[^0-9.]/.test(lines[y_coord][x_coord+1]) === true && lines[y_coord][x_coord+1] !== undefined) { return true }
}

// console.log(masterNumber)

masterNumber = main(lines)