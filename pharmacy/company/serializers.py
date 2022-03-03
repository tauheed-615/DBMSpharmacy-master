from .models import *
from rest_framework import serializers
from overview.serializers import PharmacySerializer

class StockSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySerializer(read_only=True)
    class Meta:
        model = Stock
        fields = ('id','name', 'pharmacy', 'desc','unit' )

class StockItemSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = StockItem
        fields = ('id','name', 'stock', 'desc','cost_per_tab','type','unit' )

class CompanySerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ('id','name', 'stock', 'desc' ,'type')
