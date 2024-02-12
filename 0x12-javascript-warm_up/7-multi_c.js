#!/usr/bin/node
// Prints 'C is fun' as many times as the arg passed

const args = process.argv;
const numb = parseInt(args[2], 10);
if (isNaN(numb)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
