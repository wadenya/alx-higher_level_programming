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
      let q = '';
      for (let p = 0; p < this.width; p++) {
        q += 'X';
      }
      console.log(q);
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
