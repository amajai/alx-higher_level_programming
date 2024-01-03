#!/usr/bin/node
const request = require('request');

const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  console.log(data['title'])
});
