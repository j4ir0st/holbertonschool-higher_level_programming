#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list2 = list.map((element, index) => element * index);
console.log(list2);
