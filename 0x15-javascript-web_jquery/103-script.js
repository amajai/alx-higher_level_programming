$(document).ready(function () {
  function translate () {
    const code = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  }
  $('input#btn_translate').click(translate);
  $('input#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});
