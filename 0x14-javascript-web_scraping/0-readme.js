#!/usr/bin/node
const file = require('file');
file.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
