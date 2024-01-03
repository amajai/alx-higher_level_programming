#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
let count = 0;
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  for (const key of data.results) {
    for (const charLink of key.characters) {
      if (charLink === character) {
        count += 1;
      }
    }
  }
  console.log(count);
});
