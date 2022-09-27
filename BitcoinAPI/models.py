from django.db import models


class Bitcoin(models.Model):
    name = models.CharField(max_length=100, default='Bitcoin')
    price = models.DecimalField(decimal_places=6, max_digits=100, default=0.0)
    currency = models.CharField(max_length=50, default='inr')
    created_on = models.DateTimeField(auto_now=True)
