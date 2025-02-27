from django.db import models

class TourType(models.Model):
    name = models.CharField(max_length=255)
    type_img = models.TextField()

    def __str__(self):
        return self.name
