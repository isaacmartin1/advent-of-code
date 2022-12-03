const fs = require("fs")

let lines = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function solve() {
    let score = 0
    const alphabetList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (let i=0; i<lines.length; i = i+3) {
        // accommate for extra line at end
        if(lines[i].length === 0) {
            break;
        }
        const elf1 = lines[i]
        const elf2 = lines[i+1]
        const elf3 = lines[i+2]
        let common_letter = identifyCommonLetter(elf1, elf2, elf3)
        const letterValue = findValueOfLetter(common_letter, alphabetList)
        score += letterValue  
    }
    return score;
}

function findValueOfLetter(common_letter, alphabetList) {
    for (let x=0; x<alphabetList.length; x++) {
        if (common_letter === alphabetList[x]) {
            return x+1;
        }
    }
}

function identifyCommonLetter(elf1, elf2, elf3) {
    for (let z=0; z<elf1.length; z++) {
        for (let y=0; y<elf2.length; y++) {
            for (let x=0; x<elf3.length; x++) {
                if (elf1[z] === elf2[y] && elf2[y]===elf3[x]) {
                    return elf1[z];
                };
            }
        };
    };
};

const finalResult = solve();
console.log(finalResult)