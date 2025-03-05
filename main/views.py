from django.shortcuts import render
from main.models import TourType

def open_main(request):
    tour_types = TourType.objects.all()
    return render(request, 'main.html', {'tour_types': tour_types})
