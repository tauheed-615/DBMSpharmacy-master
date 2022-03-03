from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route, api_view, authentication_classes, permission_classes
# Create your views here.

def response_500(log_msg, e):

    return Response({'status': 'error','message': 'Something went wrong.'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_400(message, log_msg, e):

    return Response({'status': 'error','message': message}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_stock(request , pharmacy_id):

        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        if 'name' in request.data :
            stock = Stock()
            stock.name = name
            stock.pharmacy = pharmacy
            stock.desc = desc
            stock.unit = unit
            stock.save()
            return Response(StockSerializer(stock).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Stock name not found in request.", "Stock name not found in request.", None)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_stocks(request , pharmacy_id ):
        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        stocks=Stock.objects.filter(pharmacy = pharmacy)
        return Response(StockSerializer(stocks, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_stock_item(request ,  stock_id):

        stock = Stock.objects.get(id = stock_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        cost_per_tab = request.data['cost']
        type = request.data['type']
        if 'name' in request.data :
            stock_item = StockItem()
            stock_item.name = name
            stock_item.stock = stock
            stock_item.desc = desc
            stock_item.unit = unit
            stock_item.save()
            return Response(StockItemSerializer(stock_item).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Stock item name not found in request.", "Stock item name not found in request.", None)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_stock_items(request , stock_id ):
        stock = Stock.objects.get(id = stock_id)
        stock_items=StockItem.objects.filter(stock = stock)
        return Response(StockItemSerializer(stocks, many=True).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_stock(request , pharmacy_id):

        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        name = request.data['name']
        desc = request.data['desc']
        type = request.data['type']
        stock.name = name
        stock.pharmacy = pharmacy
        stock.desc = desc
        stock.type = type
        stock.save()
        return Response(StockSerializer(stock).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_stock_item(request ,  stock_item_id):

        stock_item = StockItem.objects.get(id = stock_item_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        cost_per_tab = request.data['cost']
        type = request.data['type']
        stock_item.name = name
        stock_item.desc = desc
        stock_item.unit = unit
        stock_item.save()
        return Response(StockItemSerializer(stock_item).data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_stock(request, stock_id):
    try:
        Stock.objects.get(id=stock_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Stock not found.", "Error while deleting stock from database.", e)

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_stock_item(request, stock_item_id):
    try:
        StockItem.objects.get(id=stock_item_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Stock item not found.", "Error while deleting stock item from database.", e)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_company(request ,  stock_id):

        stock = Stock.objects.get(id = stock_id)
        name = request.data['name']
        desc = request.data['desc']
        type = request.data['type']
        if 'name' in request.data :
            company = Company()
            company.name = name
            company.stock = stock
            company.desc = desc
            company.type = type
            company.save()
            return Response(CompanySerializer(company).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Company name not found in request.", "Company name not found in request.", None)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_company(request ,  company_id):

        company = Company.objects.get(id = company_id)
        name = request.data['name']
        desc = request.data['desc']
        type = request.data['type']
        company.name = name
        company.desc = desc
        company.type = type
        company.save()
        return Response(CompanySerializer(company).data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_company(request, company_id):
    try:
        Company.objects.get(id=company_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Company not found.", "Error while deleting company from database.", e)
