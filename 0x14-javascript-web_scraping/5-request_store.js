#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(response => {
    fs.writeFile(process.argv[3], response.data, 'utf-8', err => {
      if (err) console.log(err);
    });
  })
  .catch(err => console.log('code: ' + err.response.status));
