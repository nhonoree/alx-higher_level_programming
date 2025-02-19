// Use jQuery to add event listeners for adding, removing, and clearing list items
$(document).ready(function() {
  // Add a new <li> element when DIV#add_item is clicked
  $('#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Remove the last <li> element when DIV#remove_item is clicked
  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Clear all <li> elements when DIV#clear_list is clicked
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
