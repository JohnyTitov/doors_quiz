from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from .models import PageShop
from .forms import SelectForm


def test_bootstrap(request):
    if request.method == 'GET':
        form = SelectForm()
        return render(request, 'index.html', {'form': form,})
    elif request.method == 'POST':
        return redirect('/')


def show_page(request, url_name):
    if request.method == 'GET':
        # получить страницы с данным именем
        pages = PageShop.objects.filter(name_page=url_name)

        if pages.count() > 0:                                 # если есть
            shop = pages[0]                                   # выбрать первую

            form = SelectForm()
            param = {'shop': shop,                            # заполнить параметры
                     'url_name': url_name,
                     'form': form, }
            return render(request, 'index.html', param)
        else:
            return redirect('/')
    elif request.method == 'POST':
        return redirect('/')
