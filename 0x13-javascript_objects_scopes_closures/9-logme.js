#!/usr/bin/node

let nmbarg = 0;

exports.logMe = function (item) {
  console.log(nmbarg + ': ' + item);
  nmbarg++;
};
