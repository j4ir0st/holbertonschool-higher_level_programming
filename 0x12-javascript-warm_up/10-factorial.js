#!/usr/bin/node
const { argv } = require('process');
function factorial (n) {
  if (n < 2 || isNaN(n)) {
    return (1);
  }
  return (n * (factorial(n - 1)));
}
const myNumb = parseInt(argv[2]);
let fact = 0;
fact = factorial(myNumb);
console.log(fact);
