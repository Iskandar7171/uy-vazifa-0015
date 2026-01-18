from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order,OrderItem
from .serializer import OrderSerializer,OrderItemSerializer
# Create your views here.

class OrderApiView(APIView):
    def get(self,request):
        order = Order.objects.all()
        data = OrderSerializer(order,many=True)
        return Response(data.data)
    
class OrderItemApiView(APIView):
    def get(self,request):
        orderitem = OrderItem.objects.all()
        data = OrderItemSerializer(orderitem,many = True)
        return Response(data.data)
    
    def post(self,request):
        new_order = OrderItem(data=request.data)
        new_order.save() 
        if new_order.is_valid():
            return Response({
                "massage": "Order qoshildi"
            })
        return Response({
            "massage": "ok"
        })


