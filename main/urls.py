from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.open_main, name='main'),
]
