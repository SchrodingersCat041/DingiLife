from django.db import models


class NearBy(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    place_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name
