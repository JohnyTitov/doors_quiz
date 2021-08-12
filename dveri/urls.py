from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ShowPage, SendMailMessage

urlpatterns = [
    path('<str:url_name>/', ShowPage),
    path('<str:url_name>/contact/', SendMailMessage),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
