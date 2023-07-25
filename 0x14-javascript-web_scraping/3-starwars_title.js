#!/usr/bin/node
const request = require("request");
const id = process.argv[2];
if (id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  });
} else console.log("Film's ID null");
