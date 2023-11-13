#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
console.log(`${args[0]} is ${args[1]}`);
