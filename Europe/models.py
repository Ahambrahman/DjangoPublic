from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    nights = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f"{self.id}- {self.origin} to {self.destination} for {self.nights} nights, costs {self.price} EUR"