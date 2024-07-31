#!/usr/bin/node

const fs = require('fs');

try {
  const filename = process.argv[2];
  const content = fs.readFileSync(filename, 'utf8');
  console.log(content);
} catch (err) {
  if (err.code === 'ENOENT') console.log(err);
  else if (err.code === 'ERR_INVALID_ARG_TYPE') console.log('filename not found!');
}
