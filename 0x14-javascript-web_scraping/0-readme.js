#!/usr/bin/node
const fs = require('fs').promises;

fs.readFile(process.argv[2], { encoding: 'utf-8' })
  .then((data) => console.log(data.toString()))
  .catch((err) => console.error(err));
