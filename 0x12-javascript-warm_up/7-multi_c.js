#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
if (!parseInt(args[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
