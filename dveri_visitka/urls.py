from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dveri.urls')),
    path('site/admin/', admin.site.urls),
]
