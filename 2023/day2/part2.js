const fs = require("fs")

let lines = fs.readFileSync("input.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

let masterNumber = 0

function cleanSpaces (array) {
    for (let i = 0; i < array.length; i++) {
        array[i] = array[i].replaceAll(' ', '')
    }
    return array
}

function solve (array) {
    let minBlue = 0
    let minRed = 0
    let minGreen = 0
    for (i=0; i<array.length; i++) {
        split = array[i].split(/,/)
        split = cleanSpaces(split)
        for ( let x = 0; x < split.length ; x++) {
            let workingVersion = split[x].split(/(\d+)/)
            console.log(workingVersion)
            if (Number(workingVersion[1]) > minGreen && workingVersion[2] == 'green') {minGreen = Number(workingVersion[1])}

            if (Number(workingVersion[1]) > minBlue && workingVersion[2] == 'blue') {minBlue = Number(workingVersion[1])}

            if (Number(workingVersion[1]) > minRed && workingVersion[2] == 'red') {minRed = Number(workingVersion[1])}
        }    
    }
    console.log(minBlue, minRed, minGreen)

    // console.log(power)
    return minBlue * minRed * minGreen
}

for (x=0; x < lines.length; x++) {
    let splitArray = lines[x].split(/:/)
    let content = splitArray[1]
    let draw = content.split(/;/)
    let power = solve(draw)
    // for (i=0; i<draw.length; i++) {
    //     split = draw[i].split(/,/)
    //     split = cleanSpaces(split)
    //     console.log(split)
    //     // power = solve(split)
    // }
    console.log(power)
    masterNumber += power
}

console.log(masterNumber)
