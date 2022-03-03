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
@permission_classes([IsAuthenticated])
def add_drug(request , pharmacy_id):

        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        name = request.data['name']
        unit = request.data['unit']
        desc = request.data['desc']
        cost_per_tab = request.data['cost']
        type = request.data['type']
        if 'name' in request.data :
            drug = Drug()
            drug.name = name
            drug.pharmacy = pharmacy
            drug.unit = unit
            drug.desc = desc
            drug.cost_per_tab = cost_per_tab
            drug.type = type
            drug.save()
            return Response(DrugSerializer(drug).data, status=status.HTTP_201_CREATED)
        else:
            return response_400("Drug name not found in request.", "Drug name not found in request.", None)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
@permission_classes([IsAuthenticated])
def edit_drug(request ,  drug_id):
        drug = Drug.objects.get(id = drug_id)
        name = request.data['name']
        unit = request.data['unit']
        desc = request.data['desc']
        cost_per_tab = request.data['cost']
        type = request.data['type']
        drug.name = name
        drug.unit = unit
        drug.desc = desc
        drug.cost_per_tab = cost_per_tab
        drug.type = type
        drug.save()
        return Response(DrugSerializer(drug).data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_drug(request ,  drug_id):
        drug= Drug.objects.get(id = drug_id)
        if  drug.unit==1:
                drug.delete()
                return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
                drug=Drug.objects.get(id = drug_id)
                drug.unit=drug.unit-1
                drug.save()
                return Response(DrugSerializer(drug).data, status=status.HTTP_200_OK)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_drugs(request , pharmacy_id ):
        pharmacy = Pharmacy.objects.get(id = pharmacy_id)
        drugs=Drug.objects.filter(pharmacy = pharmacy)
        return Response(DrugSerializer(drugs, many=True).data, status=status.HTTP_200_OK)
