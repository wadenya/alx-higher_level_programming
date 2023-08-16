#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      let s = '';
      for (let d = 0; d < this.width; d++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const flip = this.width;
    this.width = this.height
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
