#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined){
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sq = '';
      for (let p = 0; p < this.width; p++) {
        sq += c;
      }
      console.log(sq);
    }
  }
}

module.exports = Square;
