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
    for ( let x = 0; x < array.length ; x++) {
        let workingVersion = array[x].split(/(\d+)/)
        if (Number(workingVersion[1]) > 12 && workingVersion[2] == 'red') { console.log('fail red', workingVersion) 
        return false }
        if (Number(workingVersion[1]) > 13 && workingVersion[2] == 'green') { console.log('fail green', workingVersion)
            return false }
        if (Number(workingVersion[1]) > 14 && workingVersion[2] == 'blue') { console.log('fail blue', workingVersion)
            return false }
    }
    // console.log(array, 'is verifiably valid')
    return true
}

for (x=0; x < lines.length; x++) {
    let splitArray = lines[x].split(/:/)
    let game = splitArray[0]
    let id = Number(game.split(/(\d+)/)[1])
    console.log(id)
    let content = splitArray[1]
    let draw = content.split(/;/)
    let record = true
    for (i=0; i<draw.length; i++) {
        split = draw[i].split(/,/)
        split = cleanSpaces(split)
        let condition = solve(split)
        if (condition == false) { record = false}
    }
    if (record == true) {
        console.log(id)
        masterNumber += id
    }
}

console.log(masterNumber)
