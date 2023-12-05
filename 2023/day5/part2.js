const fs = require("fs")

let lines = fs.readFileSync("input.csv", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function main(lines) {
    console.log(lines)
    
}

masterNumber = main(lines)