const fs = require("fs")


let lines = fs
    .readFileSync("day1.txt", {encoding: "utf-8"})
    .split('\n')
    .map((x) => parseInt(x))

let total = 0;




for (let i = 0; i < lines.length-2; i++) {
        let prior = lines[i] + lines[i+1] + lines[i+2];
        let current = lines[i+1] + lines[i+2] + lines[i+3];
        if (current > prior) {
            total++;
        }
    }

// 7:02
console.log(total)


// Part 2
//8:53, shown above