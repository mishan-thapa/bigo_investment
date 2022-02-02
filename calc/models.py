from pyexpat import model
from django.db import models

# Create your models here.

# class TSLA(models.Model):
#     Date = models.DateField()
#     Open = models.FloatField(max_length=20)
#     High = models.FloatField(max_length=20)
#     Low = models.FloatField(max_length=20)
#     Close = models.FloatField(max_length=20)
#     Adjusted_Close = models.FloatField(max_length=20)
#     Volume = models.IntegerField()

class fundamental(models.Model):
    companies = models.TextField()
    trailing_PE = models.FloatField(max_length=20)
    return_on_equity = models.FloatField(max_length=20)
    return_on_assets = models.FloatField(max_length=20)
    book_value = models.FloatField(max_length=20)
    trailing_EPS = models.FloatField(max_length=20)
    price_to_book = models.FloatField(max_length=20)
    sector = models.TextField()
    payout_ratio = models.FloatField(max_length=20)
    market_cap = models.BigIntegerField()
    trailing_peg_ratio = models.FloatField(max_length=20)

    def __str__(self):
      return self.companies

class a(models.Model):

    date = models.DateField()
    open = models.FloatField(max_length=20)
    high = models.FloatField(max_length=20)
    low = models.FloatField(max_length=20)
    close = models.FloatField(max_length=20)
    adj_close = models.FloatField(max_length=20)
    volume = models.IntegerField()
    rsi = models.FloatField(max_length=20)
    macd = models.TextField()
    bollingerband_signal = models.TextField()
    

    def __str__(self):
      return self.date