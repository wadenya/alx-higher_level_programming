#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const h in valsUniq) {
  const list = [];
  for (const c in totalist) {
    if (totalist[c][1] === valsUniq[h]) {
      list.unshift(totalist[c][0]);
    }
  }
  newDict[valsUniq[h]] = list;
}
console.log(newDict);
