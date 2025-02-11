#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch movie data
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Fetch and print each character's name in order
    const fetchCharacter = (index) => {
      if (index >= characters.length) return;

      request(characters[index], (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
          fetchCharacter(index + 1); // Fetch the next character
        }
      });
    };

    fetchCharacter(0); // Start fetching from the first character
  }
});
