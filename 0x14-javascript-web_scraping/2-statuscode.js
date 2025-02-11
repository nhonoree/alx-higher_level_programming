#!/usr/bin/node

const request = require('request');

// Get the URL from command line arguments
const url = process.argv[2];

// Make a GET request and print the status code
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
