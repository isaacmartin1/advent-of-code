const fs = require("fs")

let line = fs.readFileSync("input.txt", {encoding: "utf-8"})

function part1(line) {
    let total = 0
    for (let i = 0; i < line.length; i++) {
        total += 1
        if (line[i] !== line[i+1] &&
            line[i] !== line[i+2] &&
            line[i] !== line[i+3] &&
            line[i+1] !== line[i+2] &&
            line[i+1] !== line[i+3] &&
            line[i+2] !== line[i+3]) {
                total += 3
                break;
            }
    }
    return total
}

let part1answer = part1(line)
console.log(part1answer)

function part2(line) {
    let total = 0
    for (let i = 0; i < line.length; i++) {
        total += 1
        let currentGroup = []
        for (let x = 0; x < 14; x++) {
            if (x > 0) {
                if (currentGroup.includes(line[i+x])) {
                    currentGroup = []
                    continue;
                } else {
                    currentGroup.push(line[i+x])
                }
            } else {
                currentGroup.push(line[i+x])
            }
        }

        if (currentGroup.length === 14) {
            total += 13
            break;
        }

    }
    return total
}

let part2answer = part2(line)
console.log(part2answer)