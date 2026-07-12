#!/usr/bin/node

const args = Number(process.argv[2]);

function factorial (n) {
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}
console.log(factorial(args));
