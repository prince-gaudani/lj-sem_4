from django.db import models

# Create your models here.
class News(models.Model):
    headLine=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField()
    url=models.URLField(blank=True)