// Use jQuery to add a click event listener to DIV#add_item
$('#add_item').click(function() {
  // Append a new <li> element with the text "Item" to UL.my_list
  $('ul.my_list').append('<li>Item</li>');
});
