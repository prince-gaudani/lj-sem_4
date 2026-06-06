from django.db import models

# Create your models here.
class Events(models.Model):
    EventName=models.TextField()
    EventDate=models.DateField()
    Location=models.TextField()
    Category=models.TextField()
    