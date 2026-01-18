from django.urls import path
from .views import OrderApiView,OrderItemApiView

urlpatterns = [
    path('order/',OrderApiView.as_view()),
    path('orderitem/',OrderItemApiView.as_view())
]