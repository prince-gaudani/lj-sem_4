from django.db import models

# Create your models here.
class Player(models.Model):
    Name=models.CharField(max_length=100)
    Test_Innings=models.IntegerField()
    Runs=models.IntegerField()
