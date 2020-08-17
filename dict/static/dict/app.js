$(document).ready(function () {
  var words = [];

  function add_word() {
    function on_word_click(e) {
      var target = $(e.target);
      const text = target.text();
      const index = words.indexOf(text);
      if (index > -1) {
        words.splice(index, 1);
      }
      $(".words-hidden").val(words.join(" "));
      target.remove();
    }
    var word = $(".words-input").val().replace(/ /g, "");
    words.push(word);
    $(".words-input").val("");
    $(".words-hidden").val(words.join(" "));
    var d = $("<p>", { id: "word-" + word, text: word, class: "added-word" });
    d.click(on_word_click);
    $(".words-container").append(d);
  }
  $(".words-input").keypress(function (e) {
    if (e.keyCode == 32) {
      add_word();
    }
    if (e.which == 13) {
      add_word();
    }
  });
});
