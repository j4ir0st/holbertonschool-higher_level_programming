#!/usr/bin/node
const axios = require('axios').default;

axios.get(process.argv[2])
    .then(response => {
	console.log(response.data)
    })
  .catch(err => console.log('code: ' + err.response.status));
