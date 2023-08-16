#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let q = '';
      for (let d = 0; d < this.width; d++) {
        q += c;
      }
      console.log(q);
    }
  }
}

module.exports = Square;
