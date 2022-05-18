#!/usr/bin/node
const axios = require('axios');

axios.get(process.argv[2])
  .then(resp => {
    const list = {};
    resp.data.forEach(task => {
      if (task.completed === true) {
        if (list[task.userId] === undefined) {
          list[task.userId] = 1;
        } else {
          list[task.userId]++;
        }
      }
    });
    console.log(list);
  })
  .catch(err => console.log(err.message));
