from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from .models import PageShop


def test_bootstrap(request):
    return render(request, 'index.html')


def show_page(request, url_name):
    # получить страницы с данным именем
    pages = PageShop.objects.filter(name_page=url_name)

    if pages.count() > 0:                                 # если есть
        shop = pages[0]                                   # выбрать первую
        param = {'shop': shop, 'url_name': url_name}      # заполнить параметры
        return render(request, 'index.html', param)
    else:
        return redirect('/')
