from django.db import models
from overview.models import Pharmacy
# Create your models here.



class Stock(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="stock")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class StockItem(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="stock_item")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    cost_per_tab = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name



class Company(models.Model):
    stock= models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
