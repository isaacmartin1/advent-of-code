const fs = require("fs")
const { listeners } = require("process")

let lines = fs.readFileSync("input.txt", {encoding: "utf-8"}).split("\n")

for (let i=0; i<lines.length; i++) {
    lines[i] = lines[i].slice(0,-1)
}

function part1(lines) {
    let directoryList = []
    let directoryPairs = []
    let fileSizes = []
    var directoryDictionary = {}
    let currentDirectory = ''
    for (let i = 0; i < lines.length; i++) {
        if (i === lines.length-1) {
            continue;
        }
        const command = lines[i].slice(0,4)


        if (command === '$ cd') {
            if (lines[i].slice(5,) === '..') {
                continue;
            } else if (lines[i].slice(5,) === '/') {
                currentDirectory = '/'
                continue;
            } else {
                directoryDictionary
                currentDirectory = lines[i].slice(5,)
                // const indexOfCurrentFolder = directoryList.find(currentDirectory)


                directoryList.push(lines[i].slice(5,))
            }
        } else if (command === '$ ls') {

        } else if (command.slice(0,3) === 'dir') {
            directoryList.push([currentDirectory, lines[i].slice(4,)])
            directoryPairs.push([currentDirectory, lines[i].slice(4,)])

        } else {
            const size = lines[i].split(" ")
            fileSizes.push([currentDirectory, size[0]])
        }
    }
    console.log(fileSizes)
    console.log(directoryList)
    let uniqueListDraft = []
    for (let i = 0; i < directoryList.length; i++) {
        if (!uniqueListDraft.includes(directoryList[i][0])) {
            // for first part of array
            if (directoryList[i][0].length !== 1 || directoryList[i][0] === '/') {
                uniqueListDraft.push(directoryList[i][0])
            // if not array, try string check
            } else if (!uniqueListDraft.includes(directoryList[i])) {
                uniqueListDraft.push(directoryList[i])
            }
        }
    }

    let uniqueList = []
    for (let i = 0; i < uniqueListDraft.length; i++) {
        uniqueList.push([uniqueListDraft[i], 0])
    }

    console.log(uniqueList)

    console.log('directory pairs',directoryPairs)

    // adds total file size directly found in each directory
    for (let i = 0; i < uniqueList.length; i++) {
        for (let z = 0; z < fileSizes.length; z++) {
            if (fileSizes[z][0] === uniqueList[i][0]) {
                // console.log(directoryList[x][0], uniqueList[i][0],
                    // Number(fileSizes[z][1]))
                uniqueList[i][1] += Number(fileSizes[z][1])
            }
        }
    }

    // add total file size from direct subdirectories

    for (let i = 0; i < uniqueList.length; i++) {
        listSoFar = []
        uniqueList = checkLowerFolder(uniqueList, uniqueList[i][0], i, directoryPairs, fileSizes)
    }

    // for (let i = 0; i < uniqueList.length; i++) {
    //     for (let x = 0; x < directoryPairs.length; x++) {
    //         if (uniqueList[i][0] === directoryPairs[x][0]) {
    //             // add total from lower directory
    //             for (let y = 0; y < fileSizes.length; y++) {
    //                 if (uniqueList[i][0] === fileSizes[y][0]) {
    //                     uniqueList[i][1] += Number(fileSizes[y][1])
    //                 }
    //             }
    //         }
    //     }
    // }




    console.log(uniqueList)

    for (let i = 0; i < uniqueList.length; i++) {
        if (uniqueList[i][1] < 100000) {
            console.log(uniqueList[i])
        }
    }

}   

// use recursive function
function checkLowerFolder(uniqueList, reference, originalIndex, directoryPairs, fileSizes) {
    let found = false
    for (let x = 0; x < directoryPairs.length; x++) {
        if (reference === directoryPairs[x][0]) {
            // add total from lower directory
            for (let y = 0; y < fileSizes.length; y++) {
                if (reference === fileSizes[y][0]) {
                    found = true;
                    uniqueList[originalIndex][1] += Number(fileSizes[y][1])
                    reference = fileSizes[y][0]
                }
            }
        }
    }
    if (found) {
        checkLowerFolder(uniqueList, reference, originalIndex, directoryPairs, fileSizes)
    }
    else {
        return uniqueList;
    }
}


let part1answer = part1(lines)
// console.log(part1answer)