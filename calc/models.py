from django.db import models

# Create your models here.

class TSLA(models.Model):
    Date = models.DateField()
    Open = models.FloatField(max_length=20)
    High = models.FloatField(max_length=20)
    Low = models.FloatField(max_length=20)
    Close = models.FloatField(max_length=20)
    Adjusted_Close = models.FloatField(max_length=20)
    Volume = models.IntegerField()