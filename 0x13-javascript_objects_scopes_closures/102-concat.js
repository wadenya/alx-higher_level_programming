#!/usr/bin/node

const fls = require('fls');

const fArg = fls.readFileSync(process.argv[2]).toString();
const sArg = fls.readFileSync(process.argv[3]).toString();
fls.writeFileSync(process.argv[4], fArg + sArg);
