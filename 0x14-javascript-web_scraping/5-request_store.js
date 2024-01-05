#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
    return;
  }

  try {
    fs.writeFileSync(file, data, { encoding: 'utf8' });
  } catch (err) {
    console.error(err);
  }
});
