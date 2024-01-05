#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const option = {
  json: true
};
request(url, option, (err, res, data) => {
  if (err) {
    console.log(err);
  }
  for (const character of data.characters) {
    request(character, option, (err, res, data) => {
      if (err) {
        console.log(err);
      }
      console.log(data.name);
    });
  }
});
