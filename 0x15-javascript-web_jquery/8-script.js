// JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

let myurl = 'https://swapi.co/api/films/?format=json';
$.get(myurl, function (data) {
  let movies = data.results;
  for (let film of movies) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
