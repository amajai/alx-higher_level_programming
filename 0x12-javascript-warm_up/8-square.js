#!/usr/bin/node
const { argv } = require('node:process');
const [, , ...args] = argv;
if (!parseInt(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('X'.repeat(args[0]));
  }
}
