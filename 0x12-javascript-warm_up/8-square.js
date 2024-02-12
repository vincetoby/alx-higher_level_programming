#!/usr/bin/node
// this Prnts a square of a specified size

const args = process.argv;
const dsize = parseInt(args[2], 10);
const row = [];

if (isNaN(dsize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < dsize; i++) {
    row.push('X');
  }
  for (let i = 0; i < dsize; i++) {
    console.log(row.join(''));
  }
}
