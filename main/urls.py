from django.urls import path

from main import views



app_name = 'main'

urlpatterns = [
    path('', views.open_main, name='main'),
    path('tours', views.open_tours, name='tours'),
    path('about', views.open_about, name='about'),
    path('contact', views.open_contact, name='contact'),
    path('news', views.open_news, name='news')
]
