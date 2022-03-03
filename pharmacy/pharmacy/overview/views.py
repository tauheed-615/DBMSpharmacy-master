from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import detail_route, list_route, api_view, authentication_classes, permission_classes
from . import models
from . import serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


def response_500(log_msg, e):

    return Response({'status': 'error','message': 'Something went wrong.'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


def response_400(message, log_msg, e):

    return Response({'status': 'error','message': message}, status= status.HTTP_400_BAD_REQUEST)

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
# Create your views here.
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_pharmacy(request ):
    if request.method == 'POST':


            name = request.data['name']
            address = request.data['address']
            if 'name' in request.data :
                pharmacy = Pharmacy()
                pharmacy.name = name
                pharmacy.address = address
                pharmacy.save()
                return Response(PharmacySerializer(pharmacy).data, status=status.HTTP_201_CREATED)
            else:
                return response_400("Pharmacy name not found in request.", "Pharmacy name not found in request.", None)

    else:
            return response_400("sdjvhak")

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_pharmacy(request , pharmacy_id ):
    if request.method == 'POST':

            pharmacy = Pharmacy.objects.get(id = pharmacy_id)
            name = request.data['name']
            address = request.data['address']
            pharmacy.name = name
            pharmacy.address = address
            pharmacy.save()
            return Response(PharmacySerializer(pharmacy).data, status=status.HTTP_200_OK)


    else:
            return response_400("sdjvhak")

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_pharmacys(request):
        pharmacy=Pharmacy.objects.all()
        return Response(PharmacySerializer(pharmacy, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_pharmacy(request,pharmacy_id):
        pharmacy=Pharmacy.objects.get(id = pharmacy_id)
        return Response(PharmacySerializer(pharmacy).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_user(request,username):
        user = CustomUser.objects.get(username = username)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_users(request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_user(request,username):
        custom_user = CustomUser.objects.get(username = username)
        custom_user.username = username
        if 'name' in request.data and request.data['name'] is not '':
            custom_user.name = request.data['name']
        if 'email' in request.data and request.data['email'] is not '':
            custom_user.email = request.data['email']
        if 'address' in request.data and request.data['address'] is not '':
            custom_user.address = request.data['address']
        if 'phone' in request.data and request.data['phone'] is not '':
            custom_user.phone = int(request.data['phone'])
        custom_user.save()
        return Response(UserSerializer(custom_user).data, status=status.HTTP_200_OK)
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def set_admin(request,username):
        custom_user = CustomUser.objects.get(username = username)
        custom_user.isadmin = 'Admin'
        custom_user.save()
        return Response(UserSerializer(custom_user).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def set_user(request,username):
        custom_user = CustomUser.objects.get(username = username)
        custom_user.isadmin = 'User'
        custom_user.save()
        return Response(UserSerializer(custom_user).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_user_admin(request,username):
        custom_user = CustomUser.objects.get(username = username)
        custom_user.username = username
        custom_user.email = request.data['email']

        return Response(UserSerializer(custom_user).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def add_users(request):
        custom_user = CustomUser()
        if 'username' in request.data and request.data['username'] is not '':
            custom_user.username = request.data['username']
        if 'isadmin' in request.data and request.data['isadmin'] is not '':
            custom_user.isadmin = request.data['isadmin']
        if 'name' in request.data and request.data['name'] is not '':
            custom_user.name = request.data['name']
        if 'email' in request.data and request.data['email'] is not '':
            custom_user.email = request.data['email']
        if 'address' in request.data and request.data['address'] is not '':
            custom_user.address = request.data['address']
        if 'phone' in request.data and request.data['phone'] is not '':
            custom_user.phone = int(request.data['phone'])
        custom_user.save()
        return Response(UserSerializer(custom_user).data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_user(request ,  username):
        user= CustomUser.objects.get(username = username)
        user.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
