function btn_action(){
  let start = Date.now(); // запомнить время начала

  let timer = setInterval(function() {
    // сколько времени прошло с начала анимации?
    let timePassed = Date.now() - start;

    if (timePassed >= 2000) {
      clearInterval(timer); // закончить анимацию через 2 секунды
      return;
    }
    // отрисовать анимацию на момент timePassed, прошедший с начала анимации
    draw(timePassed);

  }, 20);
}

function draw(timePassed) {
  // Сместить блок с контентом вправа
  let div_content = document.getElementById('content-block');
  div_content.style.left = timePassed * 2 + "px";

  // Сместить блок с картинкой влево
  let div_img = document.getElementById('main-image');
  div_img.style.right = timePassed * 2 + "px";

  // Убрать все стартовые эл-ты со страницы
  if(timePassed > 1500)
  {
    let start_page = document.getElementById('start-page');
    start_page.style.display = "none";
  }
}