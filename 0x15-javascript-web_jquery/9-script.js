// Use jQuery to fetch data from the API
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
  // Display the translation of "hello" in DIV#hello
  $('#hello').text(data.hello);
});
