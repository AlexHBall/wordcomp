$(document).ready(function () {
  $(".word-link").each(function( index ) {
    var text = $( this ).text();
    console.log("Links coming soon!");
  });


  // $.ajax({
  //   url: '/ajax/validate_username/',
  //   data: {
  //     'username': username
  //   },
  //   dataType: 'json',
  //   success: function (data) {
  //     if (data.is_taken) {
  //       alert("A user with this username already exists.");
  //     }
  //   }
  // });
});
