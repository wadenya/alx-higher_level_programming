#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nmbOccurences = 0;
  for (let y = 0; y < list.length; y++) {
    if (searchElement === list[y]) {
      nmbOccurences++;
    }
  }
  return nmbOccurences;
}
