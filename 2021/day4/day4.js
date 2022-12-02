const fs = require("fs")

let lines = fs.readFileSync("day4.txt", {encoding: "utf-8"}).split("\n")    

let firstList = lines[0].split(',')

lines.splice(0,2)

// clean data by splitting on spaces
splitLines = []
for (let x = 0; x < lines.length; x++) {
    splitLines.push(lines[x].split(" "))
}

// remove extra spaces
removeSpaces = [];

for (let z = 0; z < splitLines.length; z++) {
    removeSpaces.push(splitLines[z].filter((n) => n))
}

// change strings to numbers
for (let y = 0; y < removeSpaces.length; y++) {
    for (q = 0; q < removeSpaces[y].length; q++) {
        removeSpaces[y][q] = parseInt(removeSpaces[y][q])
    }
}

// set lines equal to cleanLines
lines = removeSpaces

let activeNumbers = [];
let answer = 0;
let validItems = 0;
let currentRow = 0;
let answerList = []
let dontUseTheseRowsAnymore = []
skip = false;

function isMarked(checking, taken) {
    let subtractionTotal = 0;
    if (checking === taken) {
        subtractionTotal -= taken;
    }
    return subtractionTotal;
}

for (let u = 0; u < firstList.length; u++) {
    answer = 0;
    activeNumbers.push(parseInt(firstList[u]));
    for (let i = 0; i < lines.length; i += 6) { // check rows and columns every six rows down
        if (skip === true) {
            skip = false;
        }
        currentRow = i;
        for (let n = 0; n <  dontUseTheseRowsAnymore.length; n++) {
            if (currentRow === dontUseTheseRowsAnymore[n]) {
                skip = true;
            }
        }
        // check columns
        if (skip === false) {
        for (let n = 0; n < 5; n++) {
            validItems = 0;
            for (let v = 0; v < activeNumbers.length; v++) {
                if (lines[i][n] === activeNumbers[v]) {validItems++}
                else if (lines[i+1][n] === activeNumbers[v]) {validItems++}
                else if (lines[i+2][n] === activeNumbers[v]) {validItems++}
                else if (lines[i+3][n] === activeNumbers[v]) {validItems++}
                else if (lines[i+4][n] === activeNumbers[v]) {validItems++}
            }
            if (validItems === 5) {
                    console.log(lines[i][n],
                        lines[i+1][n],
                        lines[i+2][n],
                        lines[i+3][n],
                        lines[i+4][n],
                        lines[i],
                        lines[i+1],
                        lines[i+2],
                        lines[i+3],
                        lines[i+4]);
                    for (let p = currentRow; p < currentRow+5; p++) {
                        for (let e = 0; e < 5; e++) {
                            answer += lines[p][e];
                        }
                    }
                    // subtract marked numbers -- this is the part that hasn't been working
                    for (let p = currentRow; p < currentRow+5; p++) {
                        for (let e = 0; e < 5; e++) {
                            let currentItem = lines[p][e]
                            for (let i = 0; i < activeNumbers.length; i++) {
                                answer += isMarked(currentItem, activeNumbers[i])
                            }
                        }
                    }
                    answer *= activeNumbers.at(-1);
                    //break; // comment out breaks for part 2
                    answerList.push(answer);
                    dontUseTheseRowsAnymore.push(currentRow);
                    answer = 0;
                }
        }
        // check rows
        for (let c = 0; c < 5; c++) {
            counter = c + currentRow;
            validItems = 0;
            for (let v = 0; v < activeNumbers.length; v++) {
                if (lines[counter][0] === activeNumbers[v]) {validItems++}
                else if (lines[counter][1] === activeNumbers[v]) {validItems++}
                else if (lines[counter][2] === activeNumbers[v]) {validItems++}
                else if (lines[counter][3] === activeNumbers[v]) {validItems++}
                else if (lines[counter][4] === activeNumbers[v]) {validItems++}
            }
            if (validItems === 5) {
                console.log("FIVE IN A ROW")
                for (let p = currentRow; p < currentRow+5; p++) {
                    for (let e = 0; e < 5; e++) {
                        answer += lines[p][e];
                    }
                }
                for (let p = currentRow; p < currentRow+5; p++) {
                    for (let e = 0; e < 5; e++) {
                        let currentItem = lines[p][e]
                        for (let i = 0; i < activeNumbers.length; i++) {
                            answer += isMarked(currentItem, activeNumbers[i])
                        }
                    }
                }                
                answer *= activeNumbers.at(-1);
                answerList.push(answer);
                dontUseTheseRowsAnymore.push(currentRow);
                answer = 0;
                /*break;
            }
        }
        if (answer > 0) {
            break;
        }
    }
    if (answer > 0) {
        break;
    }*/
                }   
            }
        }
    }
}

// part 1: 2 h 54m. code not done yet. took 8m 50s longer to fix code
console.log(answerList)

// part 2: done in 35m 48s
console.log(answerList.reverse())

