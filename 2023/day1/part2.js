const fs = require("fs")

let lines = fs.readFileSync("test.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

let masterNumber = 0

function evaluateNumber(character) {
    if (character === '1' || character === '2' || character === '3' || character === '4' || character === '5' || character === '6' || character === '7' || character === '8' || character === '9') return true
}

function findFirstNumber(line) {
    let characters = []
    for (let x = 0; x < line.length; x++) {
        characters.push(line[x])

        if (characters.join('').includes('one')) {
           return(1)
        }
        if (characters.join('').includes('two')) {
           return(2)
        }
        if (characters.join('').includes('three')) {
           return(3)
        }
        if (characters.join('').includes('four')) {
           return(4)
        }
        if (characters.join('').includes('five')) {
           return(5)
        }
        if (characters.join('').includes('six')) {
           return(6)
        }
        if (characters.join('').includes('seven')) {
           return(7)
        }
        if (characters.join('').includes('eight')) {
           return(8)
        }
        if (characters.join('').includes('nine')) {
           return(9)
        }
        if (evaluateNumber(line[x])) {
           return(Number(line[x]))
        }
    }
}

function findLastNumber(line) {
    let characters = []
    for (let x = line.length-1; x > 0; x--) {
        characters.unshift(line[x])
        if (characters.join('').includes('one')) {
           return(1)
        }
        if (characters.join('').includes('two')) {
           return(2)
        }
        if (characters.join('').includes('three')) {
           return(3)
        }
        if (characters.join('').includes('four')) {
           return(4)
        }
        if (characters.join('').includes('five')) {
           return(5)
        }
        if (characters.join('').includes('six')) {
           return(6)
        }
        if (characters.join('').includes('seven')) {
           return(7)
        }
        if (characters.join('').includes('eight')) {
           return(8)
        }
        if (characters.join('').includes('nine')) {
           return(9)
        }
        if (evaluateNumber(line[x])) {
           return(Number(line[x]))
        }
    }
}

function combine(num1, num2, masterNumber) {
    return masterNumber = Number(num1+num2)
}


function parseIntegerList(line) {
    let integerList = []
    let characters = []
    for (let x = 0; x < line.length; x++) {
        characters.push(line[x])
        if (characters.join('').includes('one')) {
            integerList.push(1)
            characters = []
        }
        if (characters.join('').includes('two')) {
            integerList.push(2)
            characters = []
        }
        if (characters.join('').includes('three')) {
            integerList.push(3)
            characters = []
        }
        if (characters.join('').includes('four')) {
            integerList.push(4)
            characters = []
        }
        if (characters.join('').includes('five')) {
            integerList.push(5)
            characters = []
        }
        if (characters.join('').includes('six')) {
            integerList.push(6)
            characters = []
        }
        if (characters.join('').includes('seven')) {
            integerList.push(7)
            characters = []
        }
        if (characters.join('').includes('eight')) {
            integerList.push(8)
            characters = []
        }
        if (characters.join('').includes('nine')) {
            integerList.push(9)
            characters = []
        }
        if (evaluateNumber(line[x])) {
            integerList.push(Number(line[x]))
        }
    }
    return integerList
}


for (let i=0; i<lines.length; i++) {
    let firstNumber = findFirstNumber(lines[i])
    let lastNumber = findLastNumber(lines[i])
    let integerList = parseIntegerList(lines[i])
    let firstDigit = String(firstNumber)
    let lastDigit = String(lastNumber)

    if (integerList.length > 1) {
        masterNumber += combine(firstDigit, lastDigit, masterNumber)
    } else {
        masterNumber += combine(firstDigit, firstDigit, masterNumber)
    }
}

console.log(masterNumber)
