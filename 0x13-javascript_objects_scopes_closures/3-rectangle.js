#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let subs = '';
    for (let i = 0; i < this.width; i++) {
      subs = subs + 'X';
    }
    for (let j = 0; j < this.width; j++) {
      console.log(subs);
    }
  }
}
module.exports = Rectangle;
