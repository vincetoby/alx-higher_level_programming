// Uses jQuery API to change color of header to red when you click on div#red_header

$('div#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
