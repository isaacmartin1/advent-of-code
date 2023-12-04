const fs = require("fs")

let lines = fs.readFileSync("test.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

// part 1 

function combine(num1, num2, masterNumber) {
    return masterNumber = Number(num1+num2)
}

function evaluateNumber(character) {
    if (character === '1' || character === '2' || character === '3' || character === '4' || character === '5' || character === '6' || character === '7' || character === '8' || character === '9') return true
    
}

let masterNumber = 0

for (let i=0; i<lines.length; i++) {
    let firstNumber = false
    let firstDigit = ''
    let lastDigit = ''
    for (let x=0; x< lines[i].length; x++) {
        let character = lines[i][x]
        if (evaluateNumber(character) && firstNumber === false) {
            firstNumber = true
            firstDigit = String(lines[i][x])
        }

        if (evaluateNumber(character) && firstNumber === true) {
            lastDigit = String(lines[i][x])
        }
    }

    masterNumber += combine(firstDigit, lastDigit, masterNumber)
}

console.log(masterNumber)
