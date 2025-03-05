from django.urls import path

from services import views

app_name = 'services'

urlpatterns = [
       path('', views.open_services, name='services'),
]