function ChekType(){
   alert("Hello world!");
}

function magic()
{
    let VhodnMas = ['.Tip', '.Nazn', '.VheshOtd', '.VnutOtd', '.VhDop', '.Cost', '.Answer'];
    let MezhkomMas = ['.Tip', '.Kak', '.KolvoDv', '.Pokr', '.MezhDop', '.Cost', '.Answer'];
    let inp = document.getElementsByName('Calc');
    for (let i = 0; i < inp.length; i++) 
    {
        if (inp[i].type == "radio" && inp[i].checked && inp[i].value=="Vhodn") 
        {   
            for (let i = 0; i < VhodnMas.length; i++)
            {
                if(document.querySelector(VhodnMas[i]).style.display !='none')
                {
                    var activeForm = VhodnMas[i];
                    document.querySelector(VhodnMas[i + 1]).style.display ='inline';
                    document.querySelector(activeForm).style.display ='none';
                    if (activeForm == '.Cost')
                    {
                        document.getElementById('Next').hidden = true;
                        document.getElementById('Back').hidden = true;
                    }
                    break;
                }
            }
            break;
        }
        if (inp[i].type == "radio" && inp[i].checked && inp[i].value=="MezhKom") 
        {   
            for (let i = 0; i < MezhkomMas.length; i++)
            {
                if(document.querySelector(MezhkomMas[i]).style.display !='none')
                {
                    var activeForm = MezhkomMas[i];
                    document.querySelector(MezhkomMas[i + 1]).style.display ='inline';
                    document.querySelector(activeForm).style.display ='none';
                    if (activeForm == '.Cost')
                    {
                        document.getElementById('Next').hidden = true;
                        document.getElementById('Back').hidden = true;
                    }
                    break;
                }
            }
            break;
        }
    }
}
function backmagic()
{
    let VhodnMas = ['.Tip', '.Nazn', '.VheshOtd', '.VnutOtd', '.VhDop', '.Cost'];
    let MezhkomMas = ['.Tip', '.Kak', '.KolvoDv', '.Pokr', '.MezhDop', '.Cost'];
    let inp = document.getElementsByName('Calc');
    for (let i = 0; i < inp.length; i++) 
    {
        if (inp[i].type == "radio" && inp[i].checked && inp[i].value=="Vhodn") 
        {   
            for (let i = 0; i < VhodnMas.length; i++)
            {
                if(document.querySelector(VhodnMas[i]).style.display !='none')
                {
                    var activeForm = VhodnMas[i];
                    document.querySelector(VhodnMas[i - 1]).style.display ='inline';
                    document.querySelector(activeForm).style.display ='none';
                    break;
                }
            }
        }
        if (inp[i].type == "radio" && inp[i].checked && inp[i].value=="MezhKom") 
        {   
            for (let i = 0; i < MezhkomMas.length; i++)
            {
                if(document.querySelector(MezhkomMas[i]).style.display !='none')
                {
                    var activeForm = MezhkomMas[i];
                    document.querySelector(MezhkomMas[i - 1]).style.display ='inline';
                    document.querySelector(activeForm).style.display ='none';
                    break;
                }
            }
        }
    }
}
