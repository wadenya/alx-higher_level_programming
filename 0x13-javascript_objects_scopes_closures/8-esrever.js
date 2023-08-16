#!/usr/bin/node
exports.esrever = function (list) {
  let lngth = list.length - 1;
  let y = 0;
  while ((lngth - y) > 0) {
    const rev = list[lngth];
    list[lnght] = list[y];
    list[y] = rev;
    y++;
    lngth--;
  }
  return list;
};
