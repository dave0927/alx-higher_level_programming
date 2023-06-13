#!/usr/bin/node

exports.converter = function (base) {
  function newBase (number) {
    return number.toString(base);
  }

  return newBase;
};
