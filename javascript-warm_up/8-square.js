#!/usr/bin/node

if (!isNaN(process.argv[2]) && Number(process.argv[2]) > 0) {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('X'.repeat(Number(process.argv[2])));
  }
} else {
  console.log('Missing size');
}
