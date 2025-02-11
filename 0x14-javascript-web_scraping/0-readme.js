#!/usr/bin/node

// Import the fs module to handle file system operations
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Please provide a file path as an argument.');
  process.exit(1);
}

// Read the file and handle errors
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurs, print the error object
    console.error(err);
  } else {
    // If the file is read successfully, print its content
    console.log(data);
  }
});
