#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
if (!args[0]) {
  console.log('No argument');
} else {
  for (const arg of args) {
    console.log(arg);
  }
}
