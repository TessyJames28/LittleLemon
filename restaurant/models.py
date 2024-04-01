from django.db import models
from .fields import IntegerRangeField


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length = 255)
    no_of_guests = IntegerRangeField(min_value=1, max_value=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = IntegerRangeField(min_value=1, max_value=6)

    def __str__(self):
        return f"{self.title} : {self.price:.2f}"