#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  const result = a + b;
  return result;
}
const myNumb1 = parseInt(argv[2]);
const myNumb2 = parseInt(argv[3]);
let suma = 0;
suma = add(myNumb1, myNumb2);
console.log(suma);
