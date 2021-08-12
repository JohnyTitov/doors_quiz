from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

from .forms import CalcForm
from .models import visitka


def ShowPage(request, url_name):
    # получаем все страницы с таким именем
    page = visitka.objects.filter(name_page=url_name)
    if page.count() > 0:
        infa = page[0]
        # выбираем первую
        return render(request, 'dveri/index.html', {'visitka': infa, 'url_name': url_name})
    else:
        return HttpResponseNotFound('')


''' Метод для формирования сообщения из данных формы '''
def MessageInForm(form):
    result = ''
    type_door = form.cleaned_data['type_door']
    if type_door == 'Input':
        result += '1) Входная дверь \n'
        result += '2) Где будет устанавливаться: ' + form.cleaned_data['target_door'] + '\n'
        result += '3) Внешняя отделка: ' + form.cleaned_data['exterior_finish'] + '\n'
        result += '4) Внутренняя отделка: ' + form.cleaned_data['interior_finish'] + '\n'
        result += '5) Дополнительные комплектующие: '# + form.cleaned_data['dop_input']
        #dop = form.cleaned_data['dop_input']
        #for d in dop:
        #    result += d
    elif type_door == 'InterRoom':
        result += '1) Межкомнатная дверь \n'
        result += '2) Тип двери: ' + form.cleaned_data['type_InterRoom'] + '\n'
        result += '3) Кол-во: ' + form.cleaned_data['quanity_doors'] + '\n'
        result += '4) Тип покрытия: ' + form.cleaned_data['type_plating'] + '\n'
        result += '5) Дополнительные комплектующие: ' #+ form.cleaned_data['dop_InterRoom']
        #dop = form.cleaned_data['dop_InterRoom']
        #for d in dop:
        #    result += d
    result += '6) Номер телефона: ' + form.cleaned_data['number_phone'] + '\n'
    result += '7) Способ связи: ' + form.cleaned_data['communication_method']
    return result


def SendMailMessage(request, url_name):
    if request.method == 'POST':
        form = CalcForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = 'двери-заказ.рф'
            message = MessageInForm(form)#form.cleaned_data['type_door']

            try:
                send_mail(subject, message, 'dveri.zakaz.message@gmail.com', ['et@vvs-kaluga.ru'])
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'dveri/thanks.html')
    else:
        # Заполняем форму
        form = CalcForm()
        # Отправляем форму на страницу
    return render(request, 'dveri/contact.html', {'form': form, 'url_name': url_name})