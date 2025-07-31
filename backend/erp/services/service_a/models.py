from django.db import models
from erp.core.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    class Meta:
        app_label = 'service_a_unique' 
    
    def __str__(self):
        return self.name