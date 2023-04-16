from django.urls import path

from .views import home_view

'''from .views import login_view, logout_view, register_view, home_view'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
