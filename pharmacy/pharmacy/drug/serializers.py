from .models import *
from rest_framework import serializers
from overview.serializers import PharmacySerializer
from datetime import datetime, timedelta

class DrugSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySerializer( read_only=True)
    class Meta:
        model = Drug
        fields = ('id','name', 'unit', 'pharmacy', 'desc' ,'cost_per_tab','type','expiry_date')
