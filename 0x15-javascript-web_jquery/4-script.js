$('div#toggle_header').click(function () {
  $('header').toggleClass(function () {
    return $(this).is('.red, .green') ? 'green red' : 'red';
  });
});
