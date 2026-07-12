#!/usr/bin/node

const args1 = process.argv[2];
const args2 = process.argv[3];

function add (a, b) {
  return a + b;
}
if (!Number(args1) || !Number(args2)) {
  console.log('NaN');
} else {
  console.log(add(Number(args1), Number(args2)));
}
