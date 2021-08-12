from django.urls import path
from .views import test_bootstrap

urlpatterns = [
    path('', test_bootstrap),
]

