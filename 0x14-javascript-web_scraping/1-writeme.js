#!/usr/bin/node

const fs = require("fs");

try {
  const filename = process.argv[2];
  const data = process.argv[3];
  fs.writeFileSync(filename, data, "utf8");
} catch (err) {
  if (err.code === "ERR_INVALID_ARG_TYPE")
    console.log("0 or not all arguments supply");
  else if (err.code instanceof Error) console.log(err);
}
