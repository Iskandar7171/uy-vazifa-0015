from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class status(models.TextChoices):
        pending = "pending", "Kutilmoqda"
        paid = "paid", "To'landi"
        shipped = "shipped", "Jo'natilgan"
        cancelled = "cancelled", "Bekor qilindi"
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} | {self.total_price}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    def total(self):
        return f"{self.quantity} | {self.price}"
    

    

        