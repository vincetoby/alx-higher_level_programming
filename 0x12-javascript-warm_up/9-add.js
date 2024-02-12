#!/usr/bin/node
// this script prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const args = process.argv;
const numb1 = parseInt(args[2], 10);
const numb2 = parseInt(args[3], 10);

console.log(add(numb1, numb2));
