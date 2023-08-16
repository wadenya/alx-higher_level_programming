#!/usr/bin/node

exports.converter = function (base) {
  return function (numb) {
    return numb.tostring(base);
  };
};
