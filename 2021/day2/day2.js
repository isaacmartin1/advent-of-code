const fs = require("fs")

let lines = fs.readFileSync("day2.txt", {encoding: "utf-8"}).split("\n")
console.log(lines)
let horizontal = 0;
let depth = 0;
let aim = 0;

for (let i = 0; i < lines.length; i++) {
    if (lines[i].slice(0, -2) === "forward") {
        horizontal += parseInt(lines[i].slice(-2));
        depth += parseInt(lines[i].slice(-2))*aim;
    }
    else if (lines[i].slice(0, -2) === "down") {
        aim += parseInt(lines[i].slice(-2));
    }
    else if (lines[i].slice(0, -2) === "up") {
        aim -= parseInt(lines[i].slice(-2));
}
}

console.log(horizontal*depth);

// part 1: 11:33
// part 2: 13:33