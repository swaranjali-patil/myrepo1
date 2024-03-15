const image1 = document.querySelector('.image1');
const image2 = document.querySelector('.image2');
const hover = document.querySelector('.hover');
const modal = document.querySelector('.modal');
const close = document.querySelector('.close');

function show() {
  hover.classList.add('active');
  modal.classList.add('show');
}
function hide() {
  hover.classList.remove('active');
  modal.classList.remove('show');
}

image1.addEventListener('click', show)
close.addEventListener('click', hide)

image2.addEventListener('click', show)
close.addEventListener('click', hide)

// function open-img(){
//     getElementById(img1)
// }


// third comparison slider
function initComparisons1() {
  var x, i;
  x = document.getElementsByClassName("img-comp-overlay1");
  for (i = 0; i < x.length; i1++) {
    compareImages(x[i]);
  }
  function compareImages(img) {
    var slider, img, clicked = 0, w, h;
    w = img.offsetWidth
    h = img.offsetHeight;
    img.style.width = (w / 2) + "px";
    slider = document.createElement("DIV");
    slider.setAttribute("class", "img-comp-slider")
    img.parentElement.insertBefore(slider, img);
    slider.style.top = (h / 2) - (slider.offsetHeight / 2) + "px";
    slider.style.left = (w / 2) - (slider.offsetWidth / 2) + "px";
    slider.addEventListener("mousedown", slideReady);
    window.addEventListener("mouseup", slideFinish);
    slider.addEventListener("touchStart", slideReady);
    window.addEventListener("touchend", slideFinish);

    function slideReady(e) {
      e.preventDefault();
      clicked= 1;
      window.addEventListener("mousemove", slideMove);
      window.addEventListener("touchmove", slideMove);

    }
    function slideFinish() {
      clicked = 0;
    }
    function slideMove(e) {
      var pos;
      if (clicked == 0) return false;
      pos = getCursorPos(e)
      if (pos < 0) pos = 0;
      if (pos > w) pos = w;
      slide(pos);

    }
    function getCursorPos(e) {
      var a, x = 0;
      e = (e.changedTouches) ? e.changedTouches[0] : e;
      a = img.getBoundingClientRect();
      x = e.pageX - a.left;
      x = x - window.pageXOffset;
      return x;
    }
    function slide(x) {
      img.style.width = x + "px";
      slider.style.left = img.offsetWidth - (slider.offsetWidth / 2) + "px";
    }


  }

}

function initComparisons2() {
  var x2, i2;
  x2 = document.getElementsByClassName("img-comp-overlay2");
  for (i2 = 0; i2 < x2.length; i2++) {
    compareImages(x2[i2]);
  }
  function compareImages(img) {
    var slider2, img, clicked2 = 0, w2, h2;
    w2 = img.offsetWidth;
    h2 = img.offsetHeight;
    img.style.width = (w2 / 2) + "px";
    slider2 = document.createElement("DIV");
    slider2.setAttribute("class", "img-comp-slider")
    img.parentElement.insertBefore(slider2, img);
    slider2.style.top = (h2 / 2) - (slider2.offsetHeight / 2) + "px";
    slider2.style.left = (w2 / 2) - (slider2.offsetWidth / 2) + "px";
    slider2.addEventListener("mousedown", slideReady2);
    window.addEventListener("mouseup", slideFinish2);
    slider2.addEventListener("touchStart", slideReady2);
    window.addEventListener("touchend", slideFinish2);

    function slideReady2(e2) {
      e2.preventDefault2();
      clicked2 = 1;
      window.addEventListener("mousemove", slideMove2);
      window.addEventListener("touchmove", slideMove2);

    }
    function slideFinish2() {
      clicked2 = 0;
    }
    function slideMove2(e2) {
      var pos2;
      if (clicked2 == 0) return false;
      pos2 = getCursorPos2(e2)
      if (pos2 < 0) pos2 = 0;
      if (pos2 > w2) pos2 = w2;
      slide2(pos2);

    }
    function getCursorPos2(e2) {
      var a2, x2 = 0;
      e2 = (e2.changedTouches) ? e2.changedTouches[0] : e2;
      a2 = img.getBoundingClientRect2();
      x2 = e2.pageX - a2.left;
      x2 = x2 - window.pageXOffset;
      return x2;
    }
    function slide2(x2) {
      img.style.width = x2 + "px";
      slider2.style.left = img.offsetWidth - (slider2.offsetWidth / 2) + "px";
    }


  }

}


// ---------comparison slider----------
//   function changeslider1(){
//     var img = document.getElementById('home');
//     img.src = 'int34.jpg'
// }

// function changeslider2(){
//   initComparisons2();
// }

