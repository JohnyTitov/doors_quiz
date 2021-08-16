from django.urls import path
from .views import test_bootstrap, show_page

urlpatterns = [
    path('', test_bootstrap),
    path('<str:url_name>/', show_page),
]

