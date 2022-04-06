#!/usr/bin/node
const dict = require('./101-data').dict;
const dict2 = {};
Object.keys(dict).map(function (key) {
  if (dict2[dict[key]] === undefined) {
    dict2[dict[key]] = [];
  }
  dict2[dict[key]].push(key);
  return (true);
});
console.log(dict2);
