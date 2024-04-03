// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

let myurl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(myurl, function (data) {
  $('div#hello').text(data.hello);
});
