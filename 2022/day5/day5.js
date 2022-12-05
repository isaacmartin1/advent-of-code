const fs = require("fs")

let lines = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function part1(lines) {  
    // load inital part of lines
    const initialArray = []
    for (let i = 0; i < 10; i++) {
        initialArray.push(lines[i])
    }

    let formattedArray = []
    for (let i = 1; i < initialArray[0].length; i += 4) {
        const eachLineArray = []
        for (let x = 0; x < initialArray.length-1; x++) {
            eachLineArray.push(initialArray[x][i])
        }
        formattedArray.push(eachLineArray)
    }

    console.log(formattedArray)

    for (let i = 10; i < lines.length; i++) {
        // accomadate for return at end of doc
        if (i === lines.length-1) {
            break;
        }
        const formattedInstructions = lines[i].split(" ")

        // number to move
        const numberToMove = formattedInstructions[1]

        // column to take from
        const column1 = Number(formattedInstructions[3])-1

        // column to add 
        const column2 = Number(formattedInstructions[5])-1


        for (let x = 0; x < numberToMove; x++) {
            // take one from this column
            const blockToMove = checkBlock(column1, formattedArray);

            // remove the block from column 1
            formattedArray = removeBlock(column1, formattedArray);

            // add one to this colulmn
            formattedArray = addToColumn(column2, formattedArray, blockToMove)
        }
    }
    return formattedArray
}

// check which letter will be removed
function checkBlock(column1, formattedArray) {
    for (let i = 0; i < formattedArray[column1].length; i++) {
        if (formattedArray[column1][i] !== ' ') {
            return formattedArray[column1][i];
        }
    }
}

function removeBlock(column1, formattedArray) {
    for (let i = 0; i < formattedArray[column1].length; i++) {
        if (formattedArray[column1][i] !== ' ') {
            formattedArray[column1][i] = ' ';
            break;
        }
    }
    return formattedArray;
}


function addToColumn(column2, formattedArray, blockToMove) {
    // if first part of array isn't empty, just add to front of array
    if (formattedArray[column2][0] !== ' ') {
        formattedArray[column2].unshift(blockToMove)
        return formattedArray
    }
    for (let i = 0; i < formattedArray[column2].length; i++) {
        // if the column's element doesn't have a blank, go one back to the blank element
        // and add the block letter in its place
        if (formattedArray[column2][i] !== ' ') {
            formattedArray[column2][i-1] = blockToMove.toString();
            break;
        }
    }
    return formattedArray
}

const part1Answer = part1(lines)
console.log(part1Answer)


function part2(lines) {
    // load inital part of lines
    const initialArray = []
    for (let i = 0; i < 10; i++) {
        initialArray.push(lines[i])
    }

    let formattedArray = []
    for (let i = 1; i < initialArray[0].length; i += 4) {
        const eachLineArray = []
        for (let x = 0; x < initialArray.length-1; x++) {
            if (initialArray[x][i] !== ' ') {
                eachLineArray.push(initialArray[x][i])
            }
        }
        formattedArray.push(eachLineArray)
    }

    console.log(formattedArray)

    for (let i = 10; i < lines.length; i++) {
        // accomadate for return at end of doc
        if (i === lines.length-1) {
            break;
        }
        console.log(lines[i])
        const formattedInstructions = lines[i].split(" ")

        // number to move
        const numberToMove = formattedInstructions[1]

        // column to take from
        const column1 = Number(formattedInstructions[3])-1

        // column to add 
        const column2 = Number(formattedInstructions[5])-1

        // grab blocks to move
        let movedBlocks = formattedArray[column1].slice(0, numberToMove)
        console.log('after movedBlocks',formattedArray)

        // make slice permanent
        formattedArray[column1] = formattedArray[column1].slice(numberToMove,)
        console.log('after changing column 1',formattedArray)


        // add blocks to other column
        // adds blocks in order, per unshift method adding multiple
        // formattedArray[column2] = formattedArray[column2].unshift(movedBlocks)
        movedBlocks = Array.from(movedBlocks).reverse()

        for (let z = 0; z < movedBlocks.length; z++) {
            formattedArray[column2].unshift(movedBlocks[z])
        }

        console.log('after changing column 2',formattedArray)

    }
    return formattedArray
}

const part2Answer = part2(lines)
console.log(part2Answer)