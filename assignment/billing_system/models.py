from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()


class PricingTier(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    min_storage = models.PositiveIntegerField()
    max_storage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
