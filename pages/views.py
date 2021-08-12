from django.shortcuts import render


def test_bootstrap(request):
    return render(request, 'index.html')
