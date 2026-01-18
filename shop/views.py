from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category,Product
from .serializer import CategorySerializer,ProductSerializer
# Create your views here.

class CategoryApiView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        data = CategorySerializer(categories,many=True)
        return Response(data.data)
    
class ProductApiView(APIView):
    def get(self,request):
        product = Category.objects.all()
        data = ProductSerializer(product,many = True)
        return Response(data.data)
    
    def post(self,request):
        new_category = CategorySerializer(data=request.data)
        new_category.save() 
        if new_category.is_valid():
            return Response({
                "massage": "Category qoshildi"
            })
        return Response({
            "massage": "ok"
        })

