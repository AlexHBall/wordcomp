$(document).ready(function () {
  var words = [];

  function add_word() {
    var str = $(".words-input").val().replace(/ /g, "");
    words.push(str);
    console.log(words);
    $(".words-input").val("");
    $(".words-hidden").val(words.join(" "));
  }
//  TODO: add a visual aid to let the user know they've added a word
  $(".words-input").keypress(function (e) {
    if (e.keyCode == 32) {
      console.log("Spacebar pressed.");
      add_word();
    }
    if (e.which == 13) {
      add_word();
    }
  });
});
