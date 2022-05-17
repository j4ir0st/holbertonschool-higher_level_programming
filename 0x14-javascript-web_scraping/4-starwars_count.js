#!/usr/bin/node
const axios = require('axios').default;
const id = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

axios.get(process.argv[2])
  .then(resp => {
    const films = resp.data;
    for (let i = 0; i < films.count; i++) {
      if (films.results[i].characters.includes(id)) count++;
    }
    console.log(count);
  })
  .catch(err => console.log(err.message));
