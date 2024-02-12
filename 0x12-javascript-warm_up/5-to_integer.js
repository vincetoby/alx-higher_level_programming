#!/usr/bin/node
// this Prints a string only if d 1st arg can be converted to an int

const args = process.argv;
const numb = parseInt(args[2], 10);
if (isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numb}`);
}
