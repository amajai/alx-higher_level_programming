$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const code = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
    $.get(url, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
