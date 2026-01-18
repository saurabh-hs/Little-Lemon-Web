from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_quests = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    booking_date  = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.booking_date}'
    
class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'