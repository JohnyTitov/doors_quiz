function btn_action(){
  let start = Date.now(); // запомнить время начала

  let timer = setInterval(function() {
    // сколько времени прошло с начала анимации?
    let timePassed = Date.now() - start;

    if (timePassed >= 1000) {
      clearInterval(timer); // закончить анимацию через 2 секунды
      return;
    }
    // отрисовать анимацию на момент timePassed, прошедший с начала анимации
    draw(timePassed);

  }, 20);
}

function draw(timePassed) {
 
  if(timePassed < 700){
  // Сместить блок с контентом вправа
  let div_content = document.getElementById('content-block');
  div_content.style.left = timePassed * 2 + "px";

  // Сместить блок с картинкой влево
  let div_img = document.getElementById('main-image');
  div_img.style.right = timePassed * 2 + "px";
  }
  else
  {
    // Убрать все стартовые эл-ты со страницы
    let start_page = document.getElementById('start-page');
    start_page.style.display = "none";

    // Добавить эл-ты выбора
    let selection_page = document.getElementById('selection-page');
    selection_page.style.display = 'block';
    selection_page.style.opacity = timePassed/1000;
  }
}

// Начало jquery
$(document).ready(function(){

  // Отлов выбора radio
  $("input[name='type_door']").change(function(){
    var card = $('.radio-card');

    // убрать тень со всех карточек
    $.each(card, function(index, value){
      $(this).css('box-shadow', '0 0 0 0');
    });

    // Добавить тень выбранной карточке
    $(this).parent().parent().css('box-shadow', '0 0 5px 2px');
  });
});