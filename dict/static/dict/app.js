$(document).ready(function () {
  $(".words-input").keypress(function (e) {
    if (e.keyCode == 32) {
      // add word to list and remove it from textbox whilst also keeping it on the form
      console.log("Spacebar pressed.");

    }
  });
});
