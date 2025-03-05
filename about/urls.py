from django.urls import path

from .views import open_about

app_name = 'about'

urlpatterns = [
    path('', open_about, name='about'),
]

