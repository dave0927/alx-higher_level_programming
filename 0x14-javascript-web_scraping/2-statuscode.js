#!/usr/bin/node

const request = require("request");

const url = process.argv[2];
if (!url) console.log("No url found!");
else {
  request.get(url, (error, response) => {
    if (error) console.log(error);
    else console.log(`code: ${response && response.statusCode}`);
  });
}
