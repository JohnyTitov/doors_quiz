from django.urls import path
from .views import ShowPage, SendMailMessage

urlpatterns = [
    path('<str:url_name>/', ShowPage),
    path('<str:url_name>/contact/', SendMailMessage),
]

