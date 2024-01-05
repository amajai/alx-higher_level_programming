#!/usr/bin/node
const request = require('request');
const util = require('util');
const id = process.argv[2];

const promise = util.promisify(request);

const option = {
  json: true
};
(async () => {
  try {
    const data = (await promise(`https://swapi-api.alx-tools.com/api/films/${id}`, option)).body;
    for (const url of data.characters) {
      const data = (await promise(url, { json: true })).body;
      console.log(data.name);
    }
  } catch (err) {
    console.log(err);
  }
})();
