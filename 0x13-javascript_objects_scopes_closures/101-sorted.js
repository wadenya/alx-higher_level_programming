#!/usr/bin/node

const dict = require('./101-data').dict;

const allist = Object.entries(dict);
const value = Object.values(dict);
const uncVal = [...new Set(value)];
const nwDict = {};

for (const h in uncVal) {
  const list = [];
  for (const c in allist) {
    if (allist[c][1] === uncVal[h]) {
      list.unshift(allist[c][0]);
    }
  }
  nwDict[uncVal[h]] = list;
}
console.log(nwDict);
