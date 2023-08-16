#!/usr/bin/node
let nmarg = 0;

exports.logMe = function (item) {
  console.log(nmarg + ': ' + item);
  nmarg++;
};
