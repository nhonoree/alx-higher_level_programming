// Use jQuery to fetch and display the translation of "Hello"
$(document).ready(function() {
  // Function to fetch and display translation
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(url, function(data) {
      $('#hello').text(data.hello);
    });
  }

  // Add click event listener for the Translate button
  $('#btn_translate').click(fetchTranslation);

  // Add keypress event listener for the ENTER key
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // 13 is the keycode for ENTER
      fetchTranslation();
    }
  });
});
