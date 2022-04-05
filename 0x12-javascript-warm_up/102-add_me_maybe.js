#!/usr/bin/node
exports.addMeMaybe = function (a, funct) {
  a++;
  funct(a);
};
