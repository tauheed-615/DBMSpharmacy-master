from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from .models import *
from overview.models import *
from drug.models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route, api_view, authentication_classes, permission_classes
from django.core.mail import send_mail
from django.db.models import Q
from drug.serializers import DrugSerializer

# Create your views here.

def response_500(log_msg, e):

    return Response({'status': 'error','message': 'Something went wrong.'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_400(message, log_msg, e):

    return Response({'status': 'error','message': message}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
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

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_stock_user(request , pharmacy_id , username):

        user = CustomUser.objects.get(username = username)
        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        if 'name' in request.data :
            stock = UserStock()
            stock.user = user
            stock.name = name
            stock.pharmacy = pharmacy
            stock.desc = desc
            stock.unit = unit
            stock.save()
            return Response(StockSerializer(stock).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Stock name not found in request.", "Stock name not found in request.", None)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_order_by_user(request , stock_id,username):

        user = CustomUser.objects.get(username = username)
        stock = UserStock.objects.get(id = stock_id)
        total = int(request.data[str('total')])
        order = UserOrder()
        order.user=user
        order.stock = stock
        order.total = total
        total_items = UserStockItem.objects.filter(stock = stock)
        profit = 0
        for item in total_items:
            profit = profit + item.profit_per_tab
        order.total_profit = stock.unit * profit
        order.save()
        send_mail(
            'Your order '+str(order.id) +' is confirmed',
            'Order with stock '+order.stock.name + 'and Description '+order.stock.desc +' has been placed.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return Response(UserOrderSerializer(order).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_order_user(request, order_id):
    try:
        UserOrder.objects.get(id=order_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Stock item not found.", "Error while deleting stock item from database.", e)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def fulfil_order_user(request, order_id):

    order=UserOrder.objects.get(id=order_id)
    stock = order.stock
    stock_items = UserStockItem.objects.filter(stock =stock)
    for item in stock_items:
        drug = Drug.objects.get(name = item.name)
        if drug.unit>item.unit:
            drug.unit = drug.unit - stock.unit
            drug.save()
            order.fulfilled = True
            send_mail(
                'Your order '+ str(order.id) +' has been fulfilled',
                'Order with stock '+order.stock.name + ' and Description '+order.stock.desc +' has been fulfilled.Expect delivery at ' + order.user.address,
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
        else:
            return Response("Insufficient drugs", status=status.HTTP_400_BAD_REQUEST)
    order.save()
    return Response(UserOrderSerializer(order).data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_order_by_user(request,username):

        user = CustomUser.objects.get(username = username)
        orders = UserOrder.objects.filter(user = user)
        return Response(UserOrderSerializer(orders, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_user_orders(request):

        orders = UserOrder.objects.all()
        return Response(UserOrderSerializer(orders, many=True).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_order(request , stock_id):

        stock = Stock.objects.get(id = stock_id)
        total = int(request.data[str('total')])
        order = Order()
        order.stock = stock
        order.total = total
        total_items = StockItem.objects.filter(stock = stock)
        profit = 0
        for item in total_items:
            drug = Drug.objects.get(name = item.name)
            drug.unit = drug.unit + stock.unit
            profit = profit + item.profit_per_tab
        order.total_profit = stock.unit * profit
        order.company = Company.objects.get(id = request.data['company_id'])
        order.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_order(request, order_id):
    try:
        Order.objects.get(id=order_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Stock item not found.", "Error while deleting stock item from database.", e)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_stocks(request , pharmacy_id ):
        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        stocks=Stock.objects.filter(pharmacy = pharmacy)
        return Response(StockSerializer(stocks, many=True).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_stock_item(request ,  stock_id):

        stock = Stock.objects.get(id = stock_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        cost_per_tab = float(request.data['cost_per_tab'])
        type = request.data['type']
        if 'name' in request.data :
            stock_item = StockItem()
            stock_item.name = name
            stock_item.stock = stock
            stock_item.desc = desc
            stock_item.unit = unit
            stock_item.cost_per_tab = cost_per_tab
            stock_item.type = type
            stock_item.save()
            return Response(StockItemSerializer(stock_item).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Stock item name not found in request.", "Stock item name not found in request.", None)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_stock_item_user(request ,  stock_id):

        stock = UserStock.objects.get(id = stock_id)
        name = request.data['name']
        desc = request.data['desc']
        unit = int(request.data['unit'])
        cost_per_tab = float(request.data['cost_per_tab'])
        type = request.data['type']
        if 'name' in request.data :
            stock_item = UserStockItem()
            stock_item.name = name
            stock_item.stock = stock
            stock_item.desc = desc
            stock_item.unit = unit
            stock_item.cost_per_tab = cost_per_tab
            stock_item.type = type
            stock_item.save()
            return Response(UserStockItemSerializer(stock_item).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Stock item name not found in request.", "Stock item name not found in request.", None)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_stock_items(request , stock_id ):
        stock = Stock.objects.get(id = stock_id)
        stock_items=StockItem.objects.filter(stock = stock)
        return Response(StockItemSerializer(stock_items, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_stock_items_user(request , stock_id ):
        stock = UserStock.objects.get(id = stock_id)
        stock_items=UserStockItem.objects.filter(stock = stock)
        return Response(UserStockItemSerializer(stock_items, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_total_stock_items(request , stock_id ):
        total = 0
        stock = Stock.objects.get(id = stock_id)
        stock_items=StockItem.objects.filter(stock = stock)
        for item in stock_items:
            total = total + item.cost_per_tab
        total = total * stock.unit
        return Response(total, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_total_stock_items_user(request , stock_id ):
        total = 0
        stock = UserStock.objects.get(id = stock_id)
        stock_items=UserStockItem.objects.filter(stock = stock)
        for item in stock_items:
            total = total + item.cost_per_tab
        total = total * stock.unit
        return Response(total, status=status.HTTP_200_OK)

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
@authentication_classes([])
@permission_classes([])
def delete_stock_item(request, stock_item_id):
    try:
        StockItem.objects.get(id=stock_item_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Stock item not found.", "Error while deleting stock item from database.", e)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_company(request ,  stock_id):

        stock = Stock.objects.get(id = stock_id)
        name = request.data['name']
        Description = request.data['Description']
        address = request.data['address']
        if 'name' in request.data :
            company = Company()
            company.name = name
            company.stock = stock
            company.Description = Description
            company.address = address
            company.save()
            return Response(CompanySerializer(company).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Company name not found in request.", "Company name not found in request.", None)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_company_total(request):
        name = request.data['name']
        Description = request.data['Description']
        address = request.data['address']
        if 'name' in request.data :
            company = Company()
            company.name = name
            company.Description = Description
            company.address = address
            company.save()
            return Response(CompanySerializer(company).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Company name not found in request.", "Company name not found in request.", None)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def edit_company(request ,  company_id):

        company = Company.objects.get(id = company_id)
        name = request.data['name']
        address = request.data['address']
        Description = request.data['Description']

        company.name = name
        company.address = address
        company.Description = Description

        company.save()
        return Response(CompanySerializer(company).data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_company(request, company_id):
    try:
        Company.objects.get(id=company_id).delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return response_400("Company not found.", "Error while deleting company from database.", e)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_companys(request ):
        company = Company.objects.all()
        return Response(CompanySerializer(company, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_orders(request ):
        orders = Order.objects.all()
        return Response(OrderSerializer(orders, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_orders_by_company(request , company_id):
        company = Company.objects.get(id = company_id)
        if company is not None:
            orders = Order.objects.filter(company = company)
        return Response(OrderSerializer(orders, many=True).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_message(request , username):

        user = CustomUser.objects.get(username = username)
        msg = request.data['msg']
        if 'msg' in request.data and request.data['msg'] is not '' :
            message = Message()
            message.user = user
            message.msg = msg
            message.save()
            return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Message not found in request or null", "Stock name not found in request.", None)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_message(request , username):
        client = CustomUser.objects.get(username = username)
        admin = CustomUser.objects.get(username = "help")
        messages = Message.objects.filter(Q(user = client) | Q(user = admin)).order_by('date_created')
        return Response(MessageSerializer(messages, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_chat_users(request):
        users = CustomUser.objects.filter(isadmin = 'User')
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)
