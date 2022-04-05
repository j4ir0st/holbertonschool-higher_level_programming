#!/usr/bin/node
exports.callMeMoby = function (a, funct) {
  for (let i = 0; i < a; i++) {
    funct();
  }
};
