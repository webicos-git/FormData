$(function() {
  $("#filter").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $("#example-table > tbody > tr").filter(function() {      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
