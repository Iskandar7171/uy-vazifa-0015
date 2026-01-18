from rest_framework.serializers import ModelSerializer
from .models import Category,Product

class CategorySerializer(ModelSerializer):
    class Meta:
        fields = ['name','is_active','created_at']
        model = Category
        
class ProductSerializer(ModelSerializer):
    class Meta:
        fields = ['name','is_active','created_at']
        model = Product       

        