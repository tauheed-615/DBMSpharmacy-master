from django.db import models
from overview.models import Pharmacy,CustomUser
from django.utils import timezone
# Create your models here.



class Stock(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="stock")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class UserStock(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="userstock")
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="userstock")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class StockItem(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="stock_item")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    cost_per_tab = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    profit_per_tab = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return self.name

class UserStockItem(models.Model):
    stock = models.ForeignKey(UserStock, on_delete=models.CASCADE, related_name="stock_item")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    cost_per_tab = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    profit_per_tab = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return self.name



class Company(models.Model):
    stock= models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="company", blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="order")
    total = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    total_profit = models.IntegerField(default=0)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="order", blank=True, null=True)

    def __str__(self):
        return self.name

class UserOrder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="userorder")
    stock = models.ForeignKey(UserStock, on_delete=models.CASCADE, related_name="userorder")
    total = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    total_profit = models.IntegerField(default=0)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name="userorder", blank=True, null=True)
    fulfilled = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="message")
    msg =  models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.msg
