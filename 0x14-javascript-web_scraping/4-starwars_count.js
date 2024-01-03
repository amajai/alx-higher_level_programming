#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
let count;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  count = body.split('/people/18/').length - 1;
  console.log(count);
});
