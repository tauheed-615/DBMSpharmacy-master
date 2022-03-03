from django.db import models
from overview.models import Pharmacy
# Create your models here.

class Drug(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="drug")
    name = models.CharField(max_length=200, null=True)
    unit = models.IntegerField()
    desc = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    cost_per_tab = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def remove_drug(self):
        drug = Drug.objects.get(id = self.id)
        drug.unit = drug.unit - 1
        drug.save()
