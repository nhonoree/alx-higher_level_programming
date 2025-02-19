// Use jQuery to fetch data from the API
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  // Iterate over the list of movies and append each title to UL#list_movies
  data.results.forEach(function(movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
