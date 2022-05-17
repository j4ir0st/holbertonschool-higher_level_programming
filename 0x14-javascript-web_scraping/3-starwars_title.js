#!/usr/bin/node
const axios = require('axios').default;

const url = 'https://swapi-api.hbtn.io/api/films/';
axios.get(url + process.argv[2])
  .then(response => console.log(response.data.title))
  .catch(err => console.log('code: ' + err.response.status));
