from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from .models import PageShop
from .forms import SelectForm


def home(request):
    if request.method == 'GET':
        form = SelectForm()
        return render(request, 'index.html', {'form': form, })

    elif request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


def show_page(request, url_name):
    # получить страницы с данным именем
    pages = PageShop.objects.filter(name_page=url_name)     # получить страницы с данным именем
    shop = pages[0] if pages.count() > 0 else None          # выбрать перувю

    if request.method == 'GET':
        if shop:
            form = SelectForm(initial={'shop': shop})
            param = {'shop': shop,  # заполнить параметры
                     'url_name': url_name,
                     'form': form, }
            return render(request, 'index.html', param)
        else:
            return redirect(reverse('home'))        # вернуться на главную

    elif request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)
