$(document).ready(function () {
  var words = [];

  function add_word() {
    function on_word_click(e) {
      var target = $(e.target);
      var parent = target.parent();
      var text = parent.text();
      text = text.substring(0, text.length - 2);
      console.log(text);
      const index = words.indexOf(text);
      if (index > -1) {
        words.splice(index, 1);
      }
      $(".words-hidden").val(words.join(" "));
      parent.remove();
      console.log(words);
      console.log($(".words-hidden").val());
    }
    var word = $(".words-input").val().replace(/ /g, "");
    words.push(word);
    $(".words-input").val("");
    $(".words-hidden").val(words.join(" "));
    var d = $("<div>", {
      id: "word-" + word,
      text: word + " ",
      class: "added-word",
    });
    var a = $("<a>", {
      href: "javascript:void(0)",
      text: "x",
      class: "delete-word",
    });
    a.click(on_word_click);
    d.append(a);
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
