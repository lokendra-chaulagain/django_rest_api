from django.db import models

# Create your models here.


class Bike(models.Model):
    bike_name = models.CharField(max_length=100)
    bike_version = models.CharField(max_length=3)
    bike_model = models.CharField(max_length=30)

    class Meta:
        app_label = 'bike'
