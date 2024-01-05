#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const option = {
  json: true
};

request(url, option, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }
  const results = {};
  for (const task of data) {
    if (task.completed) {
      results[task.userId] = (results[task.userId] || 0) + 1;
    }
  }
  console.log(results);
});
