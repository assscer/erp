from django.db import models
from erp.core.models import BaseModel
from erp.services.service_a.models import Product

class Order(BaseModel):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='pending')
    
    class Meta:
        app_label = 'service_b_unique' 
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'service_b_unique' 
        
    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"