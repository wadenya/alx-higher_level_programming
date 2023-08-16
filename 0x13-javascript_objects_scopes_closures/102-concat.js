#!/usr/bin/node

const fls = require('fls');

const ftArg = fls.readFileSync(process.argv[2]).toString();
const scArg = fls.readFileSync(process.argv[3]).toString();
fls.writeFileSync(process.argv[4], ftArg + scArg);
