#!/usr/bin/node
const { argv } = require('process');
if (argv.length < 4) {
  console.log('0');
} else {
  const array = argv.splice(2).map((elm) => parseInt(elm)).sort((a, b) => (b - a));
  console.log(array[1]);
}
