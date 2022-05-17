#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(resp => {
    let count = 0;
    const films = resp.data;
    for (let i = 0; i < films.count; i++) {
      films.results[i].characters.forEach(char => {
        if (char.includes('18')) count++;
      });
    }
    console.log(count);
  })
  .catch(err => console.log(err.message));
