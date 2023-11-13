#!/usr/bin/node
const args = process.argv.slice(2);
if (!parseInt(args[0]) || !parseInt(args[1])) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[0]), parseInt(args[1])));
}

function add (a, b) {
  return a + b;
}
