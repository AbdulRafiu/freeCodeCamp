// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("nav-bar").style.padding = "30px 10px";
    document.getElementById("header-img").style.width = "60px";
    document.getElementById("header-img").style.height = "60px";
    document.getElementById("header-img").style.marginLeft = "30px";
  } else {
    document.getElementById("nav-bar").style.padding = "80px 10px";
    document.getElementById("header-img").style.width = "90px";
    document.getElementById("header-img").style.height = "90px";
    document.getElementById("header-img").style.marginLeft = "45px";
  }
}