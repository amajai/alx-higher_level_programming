#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);
console.log(factorial(num));


function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return factorial(n - 1) * n;
}
