// JavaScript that Fetches and replaces the name of the API data
// then replaces the name of the character in the DIV#character tag text

let my_url = 'https://swapi.co/api/people/5/?format=json';
$.get(my_url, function (data, stat) {
  $('div#character').text(data.name);
});
