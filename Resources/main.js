$(document).ready(function(){
  $("#buyAmount").prop('disabled', true);
  $("select#transactionType").change(function(){
    var selectedTransaction = $(this).children("option:selected").val(); 
    // alert(selectedTransaction);

    if (selectedTransaction == 'SELL') {
      $("#buyAmount").prop('disabled', true);
      $("#paymentRecievedToggle").prop('disabled', false);
      $("#paymentMode").prop('disabled', false);
      $("#sell-amount").prop('disabled', false);
      $("#profit-input").prop('disabled', false);
    } else if (selectedTransaction == 'BUY') {
      $("#buyAmount").prop('disabled', false);
      $("#paymentRecievedToggle").prop('disabled', true);
      $("#paymentMode").prop('disabled', true);
      $("#sell-amount").prop('disabled', true);
      $("#profit-input").prop('disabled', true);
    }
  });
});
