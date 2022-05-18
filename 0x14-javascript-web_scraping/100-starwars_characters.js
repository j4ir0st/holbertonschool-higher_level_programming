#!/usr/bin/node
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/';
axios.get(url + process.argv[2])
  .then(resp => (resp.data.characters.forEach(char => {
    const ax = require('axios').default;
    ax.get(char)
      .then(res => console.log(res.data.name))
      .catch(err => console.log(err.message));
  })))
  .catch(err => console.log(err.message));
