$(document).ready(function () {
  var words = [];

  function add_word() {
    var word = $(".words-input").val().replace(/ /g, "");
    words.push(word);
    $(".words-input").val("");
    $(".words-hidden").val(words.join(" "));
    var ps = $("p").first();
    var d = $("<div>", { id: "word-" + word, text: word, class: "added-word" });
    ps.append(d);
    //    var w = $( "[id*='word-']" )
    //   console.log(w)
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
