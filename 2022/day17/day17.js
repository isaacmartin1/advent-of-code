const fs = require("fs")

let arrows = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")[0]

function part1(arrows) {  
    let cave = ['#########']
    let fallingRock = false
    let rockShapes = ['..####.', ['...#...', '..###..', '...#...'], ['....#..', '....#..', '..###..'], []]
    for (let i = 0; i < arrows.length; i++) {
        cave = ['|.......|', 
        '|.......|', 
        '|.......|'].concat(cave)

        let currentMovement = arrows.slice(0, 1)
        arrows = arrows.slice(1, -1)
    }

    return cave
}


const part2Answer = part1(arrows)
console.log(part2Answer)
