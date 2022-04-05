#!/usr/bin/node
const { argv } = require('process');
const myNumb = parseInt(argv[2]);
let subs = '';
if (isNaN(myNumb)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    subs = subs + 'X';
  }
  for (let j = 0; j < argv[2]; j++) {
    console.log(subs);
  }
}
