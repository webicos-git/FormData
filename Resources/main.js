$(document).ready(function(){
  $("#buyAmount").prop('disabled', true);
  $("select#transactionType").change(function(){
    var selectedTransaction = $(this).children("option:selected").val();
    // alert(selectedTransaction);

    if (selectedTransaction == 'sell') {
      $("#buyAmount").prop('disabled', true);
      $("#paymentRecievedToggle").prop('disabled', false);
      $("#paymentMode").prop('disabled', false);
      $("#sell-amount").prop('disabled', false);
    } else if (selectedTransaction == 'buy') {
      $("#buyAmount").prop('disabled', false);
      $("#paymentRecievedToggle").prop('disabled', true);
      $("#paymentMode").prop('disabled', true);
      $("#sell-amount").prop('disabled', true);
    }
  });
});