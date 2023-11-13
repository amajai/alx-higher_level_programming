#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
if (!args[0]) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
