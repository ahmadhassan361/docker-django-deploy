from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework import serializers
from .serializer import ProductSerializer
# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all products': '/product',
        'single product':'/product/pk',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/product/pk/delete'
    }

    return Response(api_urls)

@api_view(['POST'])
def add_product(request):
    item = ProductSerializer(data=request.data)

    # validating for already existing data
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def view_product(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        product = Product.objects.filter(**request.query_param.dict())
    else:
        product = Product.objects.all()
    # if there is something in product else raise error
    if product:
        data = ProductSerializer(product,many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def view_single_product(request,pk=None):
    
    # checking for the parameters from the URL
    if pk is not None:
        product = Product.objects.get(pk=pk)
    # if there is something in product else raise error
    if product:
        data = ProductSerializer(product,many=False)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_product(request, pk):
    item = Product.objects.get(pk=pk)
    data = ProductSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_product(request, pk):
    item = get_object_or_404(Product, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)