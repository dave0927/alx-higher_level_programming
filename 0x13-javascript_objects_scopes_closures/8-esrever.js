#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const lIndex = list.length - 1;
  for (let i = lIndex, j = 0; i >= 0; i--, j++) {
    newList[j] = list[i];
  }
  return newList;
};
