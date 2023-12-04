const fs = require("fs")

let lines = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function part1(lines) {
    console.log(lines)
    let total = 0
    for (let i = 0; i < lines.length; i++) {
        // accomadate for return at end of doc
        if (i === lines.length-1) {
            break;
        }
        const elfList = lines[i].split(',')
        // console.log(elfList)
        const elf1Strings = elfList[0].split('-')
        const elf2Strings = elfList[1].split('-')

        const elf1 = convertArrayElementsToNumber(elf1Strings)
        const elf2 = convertArrayElementsToNumber(elf2Strings)

        if (elf1[0] >= elf2[0] && elf1[1] <= elf2[1] || elf2[0] >= elf1[0] && elf2[1] <= elf1[1]) {
            total += 1
        }
    }
    return total
}

function convertArrayElementsToNumber(array) {
    for (let i = 0; i < array.length; i++) {
        array[i] = Number(array[i])
    }
    return array
}


const part1Answer = part1(lines)
console.log(part1Answer)


function part2(lines) {
    let total = 0
    for (let i = 0; i < lines.length; i++) {
        // accomadate for return at end of doc
        if (i === lines.length-1) {
            break;
        }
        const elfList = lines[i].split(',')
        // console.log(elfList)
        const elf1Strings = elfList[0].split('-')
        const elf2Strings = elfList[1].split('-')

        const elf1 = convertArrayElementsToNumber(elf1Strings)
        const elf2 = convertArrayElementsToNumber(elf2Strings)

        if (elf1[0] >= elf2[0] && elf1[0] <= elf2[1] || // elf 1 start within elf 2
            elf1[1] <= elf2[1] && elf1[1] >= elf2[0] || // elf 1 end within elf 2
            elf2[0] >= elf1[0] && elf2[0] <= elf1[1] || // elf 2 start within elf 1
            elf2[1] <= elf1[1] && elf2[1] >= elf1[0] // elf 2 end within elf 1
            ) {
            total += 1
        }
    }
    return total
}

const part2Answer = part2(lines)
console.log(part2Answer)