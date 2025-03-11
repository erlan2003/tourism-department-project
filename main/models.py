from django.db import models

class TourType(models.Model):
    name = models.CharField(max_length=255)
    type_img = models.ImageField(upload_to='tour_types/', verbose_name="Изображение типа тура", null=True, blank=True)

    def __str__(self):
        return self.name