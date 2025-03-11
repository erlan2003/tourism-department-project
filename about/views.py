from django.shortcuts import render
from .models import AboutPage
from main.models import TourType

def about(request):
    about_page = AboutPage.objects.first()  # Берём первую запись
    tour_types = TourType.objects.all()
    return render(request, 'about/about.html', {'about_page': about_page , 'tour_types': tour_types})