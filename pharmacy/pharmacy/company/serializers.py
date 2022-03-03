from .models import *
from rest_framework import serializers
from overview.serializers import PharmacySerializer,UserSerializer

class StockSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySerializer(read_only=True)
    class Meta:
        model = Stock
        fields = ('id','name', 'pharmacy', 'desc','unit','date_created' )

class UserStockSerializer(serializers.ModelSerializer):
    pharmacy = PharmacySerializer(read_only=True)
    user = UserSerializer(read_only = True)
    class Meta:
        model = Stock
        fields = ('id','name', 'pharmacy', 'desc','unit','date_created','user' )

class StockItemSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = StockItem
        fields = ('id','name', 'stock', 'desc','cost_per_tab','type','unit' )

class UserStockItemSerializer(serializers.ModelSerializer):
    stock = UserStockSerializer(read_only=True)
    class Meta:
        model = StockItem
        fields = ('id','name', 'stock', 'desc','cost_per_tab','type','unit' )

class CompanySerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ('id','name', 'stock', 'Description' ,'address')

class UserOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stock = UserStockSerializer(read_only=True)
    class Meta:
        model = UserOrder
        fields = ('id','total', 'stock', 'total_profit' ,'date_created','user','fulfilled')

class OrderSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id','total', 'stock', 'total_profit' ,'date_created','company')

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ('id','msg','user')
