#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let k = 0; k < size; k++) row += 'X';
    console.log(row);
  }
}
