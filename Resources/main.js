console.log("Working");

$(function() {
  $("#filter").on("keyup", function() {
    let value = $(this).val().toLowerCase();
    $("#example-table > tbody > tr").filter(function() {      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

// change format of date
$(document).ready(function () {
  $('input[id$=tbDate]').datepicker({
    dateFormat: 'dd-mm-yy'			// Date Format "dd-mm-yy"
  });
});

// filter by datepicker
$(function() {
  $("#tbdate").on("change", function() {
    let value = $(this).val().toLowerCase();
    console.log(value);
    $("#example-table > tbody > tr").filter(function() {      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
