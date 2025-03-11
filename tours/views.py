from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from main.models import TourType
from tours.models import Tour

def open_tours(request, type_id):
    tour_type = get_object_or_404(TourType, id=type_id)
    tours = Tour.objects.filter(tour_type=tour_type)
    tour_types = TourType.objects.all()
    return render(request, 'tours.html', {'tours': tours, 'tour_type': tour_type, 'tour_types': tour_types})