#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
if (!isNaN(args[0])) {
  console.log('My number: ' + parseInt(args[0]));
} else {
  console.log('Not a number');
}
