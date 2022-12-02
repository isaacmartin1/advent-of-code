const fs = require("fs");

let lines = fs.readFileSync("day3.txt", {encoding: "utf-8"}).split("\n")

let gamma = [];
let epsilon = [];

let one = 0;
let two = 0
let three = 0;
let four = 0;
let five = 0;
let six = 0;
let seven = 0;
let eight = 0;
let nine = 0;
let ten = 0;
let eleven = 0;
let twelve = 0;

for (let i = 0; i < lines.length; i++) {
    for (let x = 0; x < lines[i].length; x++) {
        if (x === 0) {one += parseInt(lines[i][x])}
        else if (x === 1) {two += parseInt(lines[i][x])}
        else if (x === 2) {three += parseInt(lines[i][x])}
        else if (x === 3) {four += parseInt(lines[i][x])}
        else if (x === 4) {five += parseInt(lines[i][x])}
        else if (x === 5) {six += parseInt(lines[i][x])}
        else if (x === 6) {seven += parseInt(lines[i][x])}
        else if (x === 7) {eight += parseInt(lines[i][x])}
        else if (x === 8) {nine += parseInt(lines[i][x])}
        else if (x === 9) {ten += parseInt(lines[i][x])}
        else if (x === 10) {eleven += parseInt(lines[i][x])}
        else if (x === 11) {twelve += parseInt(lines[i][x])}
    }
}

const listOfVariables = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

for (let u = 0; u < listOfVariables.length; u++) {
    if (listOfVariables[u] > lines.length/2) {
        gamma.push(1);
        epsilon.push(0)
    }
    else if (listOfVariables[u] <= lines.length/2) {
        gamma.push(0);
        epsilon.push(1)
    }
}

console.log(gamma*epsilon)

// part 1: 41:52


// part 2
let oxygen = [];
let c02 = [];
let validItems = lines;
let counter = 0;

for (let x = 0; x < 12; x++) { // know only 12 items in list so go from 0 to 11
    for (let i = 0; i < validItems.length; i++) {
        counter += parseInt(validItems[i][x]);
        console.log(counter)
    }
    let goodItems = []
    if (counter >= validItems.length/2) {
        for (let u = 0; u < validItems.length; u++) {
            if (validItems[u][x] == 1) {goodItems.push(validItems[u])}
        }
        console.log(counter, "successfully run");
    }
    else if (counter < validItems.length/2) {
        for (let u = 0; u < validItems.length; u++) {
            if (validItems[u][x] == 0) {goodItems.push(validItems[u])}
        }
        console.log(counter, "successfully run");
    }
    validItems = goodItems;
    counter = 0;
}

oxygen = parseInt(validItems.join(""), 2)

validItems = lines

for (let x = 0; x < 12; x++) { // know only 12 items in list so go from 0 to 11
    if (validItems.length == 1) {continue}
    for (let i = 0; i < validItems.length; i++) {
        counter += parseInt(validItems[i][x]);
    }
    let goodItems = []
    if (counter >= validItems.length/2) {
        for (let u = 0; u < validItems.length; u++) {
            if (validItems[u][x] == 0) {goodItems.push(validItems[u])}
        }
        console.log(counter, "successfully run");
    }
    else if (counter < validItems.length/2) {
        for (let u = 0; u < validItems.length; u++) {
            if (validItems[u][x] == 1) {goodItems.push(validItems[u])}
        }
        console.log(counter, "successfully run");
    }
    validItems = goodItems;
    counter = 0;
}

c02 = parseInt(validItems.join(""), 2)
console.log(oxygen*c02)