from django.shortcuts import render
from .models import AboutPage

def about(request):
    about_page = AboutPage.objects.first()  # Берём первую запись
    return render(request, 'about/about.html', {'about_page': about_page})