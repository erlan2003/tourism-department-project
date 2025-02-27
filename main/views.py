from django.shortcuts import render
from main.models import TourType

def open_main(request):
    tour_types = TourType.objects.all()
    return render(request, 'main.html', {'tour_types': tour_types})

def open_tours(request):
    return render(request, 'tours.html')

def open_about(request):
    return render(request, 'about.html')

def open_contact(request):
    return render(request, 'contact.html')

def open_news(request):
    return render(request, 'news.html')