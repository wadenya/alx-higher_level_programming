#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const g in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[c][1] === valsUniq[j]) {
      list.unshift(totalist[c][0]);
    }
  }
  newDict[valsUniq[g]] = list;
}
console.log(newDict);
