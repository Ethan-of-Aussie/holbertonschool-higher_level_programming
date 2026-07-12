#!/usr/bin/node

if (process.argv[2]) {
    for (let i = 0; i < Number(process.argv[2]); i++) {
        console.log('X'.repeat(Number(process.argv[2])));
    }
} else {
    console.log('Missing size');
}
