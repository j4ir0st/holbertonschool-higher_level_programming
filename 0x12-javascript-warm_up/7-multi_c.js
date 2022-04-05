#!/usr/bin/node
const { argv } = require('process');
const myNumb = parseInt(argv[2]);
if (isNaN(myNumb)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
