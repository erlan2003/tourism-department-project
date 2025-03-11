from django.db import models
from main.models import TourType

class Tour(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание тура")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.CharField(max_length=100, verbose_name="Продолжительность", help_text="Например: 3 дня, 5 часов")
    start_location = models.CharField(max_length=255, verbose_name="Место начала тура")
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE, related_name="tours", verbose_name="Тип тура")
    image = models.ImageField(upload_to="media/tours/", verbose_name="Изображение", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name