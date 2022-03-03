
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True , max_length=255 , default='')
    phone =models.BigIntegerField(default=1234567890)
    isadmin = models.CharField(blank=True, max_length=255,default="User")

    def __str__(self):
        return self.email

class Pharmacy(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
