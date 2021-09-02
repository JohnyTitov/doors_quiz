from django.urls import path
from .views import home, show_page

urlpatterns = [
    path('', home, name='home'),
    path('<str:url_name>/', show_page),
]

