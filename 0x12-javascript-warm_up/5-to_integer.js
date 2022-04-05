#!/usr/bin/node
const { argv } = require('process');
const myNumb = parseInt(argv[2]);
if (isNaN(myNumb)) {
  console.log('Not a number');
} else {
  console.log('My number:', myNumb);
}
