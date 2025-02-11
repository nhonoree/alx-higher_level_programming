#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const url = process.argv[2];

// Make a request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeId = '18';
    let count = 0;

    // Iterate through films and count Wedge Antilles' appearances
    films.forEach((film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
