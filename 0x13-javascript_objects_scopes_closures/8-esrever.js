#!/usr/bin/node
exports.esrever = function (list) {
  const cpList = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    cpList.push(list[i]);
  }
  return cpList;
};
