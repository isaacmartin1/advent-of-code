const fs = require("fs")

let lines = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function solve() {
    let score = 0
    const alphabetList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (let i=0; i<lines.length; i++) {
        // accommate for extra line at end
        if(lines[i].length === 0) {
            break;
        }
        const middle = (lines[i].length)/2
        const rucksack1 = lines[i].slice(0,middle)
        const rucksack2 = lines[i].slice(middle,lines[i].length)
        let common_letter = identifyCommonLetter(rucksack1, rucksack2)
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

function identifyCommonLetter(rucksack1, rucksack2) {
    for (let z=0; z<rucksack1.length; z++) {
        for (let y=0; y<rucksack2.length; y++) {
            if (rucksack1[z] === rucksack2[y]) {
                return rucksack1[z];
            };
        };
    };
};

const finalResult = solve();
console.log(finalResult)