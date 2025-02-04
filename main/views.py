from django.shortcuts import render
from django.views.generic import TemplateView


def open_main(request):
    return render(request, 'main.html')


def open_tours(request):
    return render(request, 'tours.html')


def open_about(request):
    return render(request, 'about.html')

def open_contact(request):
    return render(request, 'contact.html')

def open_news(request):
    return render(request, 'news.html')