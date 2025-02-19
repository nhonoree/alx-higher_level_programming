// Use jQuery to fetch data from the API
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  // Display the character name in DIV#character
  $('#character').text(data.name);
});
