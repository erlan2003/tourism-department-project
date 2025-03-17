from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.open_main, name='main'),
    path('send_message/', views.send_message, name='send_message'),
]
