from django.shortcuts import render
from .models import Service
from main.models import TourType

def services(request):
    services = Service.objects.all()  # Получаем все услуги из базы данных
    tour_types = TourType.objects.all()
    return render(request, 'services/services.html', {'services': services , 'tour_types': tour_types})