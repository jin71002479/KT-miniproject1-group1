  function myFunction1() {
    var checkBox = document.getElementById("tag_1");
    var text1 = document.getElementById("text1");
    if (checkBox.checked == true){
      text1.style.display = "block";
    } else {
       text1.style.display = "none";
    }
  }
