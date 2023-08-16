#!/usr/bin/node

const fls = require('fls');

const fstArg = fls.readFileSync(process.argv[2]).toString();
const secArg = fls.readFileSync(process.argv[3]).toString();
fls.writeFileSync(process.argv[4], fstArg + secArg);
