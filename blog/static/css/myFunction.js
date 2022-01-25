function myFunction() {
  var checkBox = document.getElementById("tag_0");
  var text = document.getElementById("text");
  var text1 = document.getElementById("text1");
  if (checkBox.checked == true){
    text.style.display = "block";
    text1.style.display = "block";
  } else {
     text.style.display = "none";
     text1.style.display = "none";
  }
}


function myFunction10() {
var checkBox = document.getElementById("tag_10");
var text10 = document.getElementById("text10");
if (checkBox.checked == true){
  text10.style.display = "block";
} else {
    text10.style.display = "none";
}
}


function myFunction20() {
var checkBox = document.getElementById("tag_20");
var text20 = document.getElementById("text20");
if (checkBox.checked == true){
text20.style.display = "block";
} else {
  text20.style.display = "none";
}
}

