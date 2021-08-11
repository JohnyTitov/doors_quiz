$(function () {
    $("#CalculatorCarousel").carousel({
        interval : false
    });
});

$( document ).ready(function(){
$( "#ContinueBTN" ).click(function(){ // задаем функцию при нажатиии на элемент <button>
    let RadioTypes = document.getElementsByName('type_door'); 
    let InputElements = document.getElementsByClassName('InputRoom');    
    let InterElements = document.getElementsByClassName('InterRoom');

    if(RadioTypes[0].checked)
    {        
        for(let elem of InputElements)
        {
            elem.style.display ='block';
        }  
        for(let elem of InterElements)
        {
            elem.style.display ='none';
        }
    }
    if(RadioTypes[1].checked)
    {        
        for(let elem of InterElements)
        {
            elem.style.display ='block';
        }
        for(let elem of InputElements)
        {
            elem.style.display ='none';
        } 
    }
});
});