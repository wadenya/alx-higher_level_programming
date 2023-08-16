#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vls = Object.values(dict);
const vlsUniq = [...new Set(vls)];
const newDict = {};
for (const g in vlsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[c][1] === vlsUniq[j]) {
      list.unshift(totalist[c][0]);
    }
  }
  newDict[vlsUniq[g]] = list;
}
console.log(newDict);
