from django.contrib import admin

from main.models import TourType
from tours.models import Tour


admin.site.register(TourType)
admin.site.register(Tour)