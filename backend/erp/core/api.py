from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TableDataAPIView(APIView):
    """
    Универсальный API для табличных данных
    """
    def get(self, request, service_name, *args, **kwargs):
        # Здесь можно реализовать логику для разных сервисов
        if service_name == 'products':
            from erp.services.service_a.serializers import ProductSerializer
            from erp.services.service_a.models import Product
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
        elif service_name == 'orders':
            from erp.services.service_b.serializers import OrderSerializer
            from erp.services.service_b.models import Order
            queryset = Order.objects.all()
            serializer = OrderSerializer(queryset, many=True)
        else:
            return Response(
                {'error': 'Service not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        return Response({
            'data': serializer.data,
            'columns': self.get_table_columns(service_name)
        })
    
    def get_table_columns(self, service_name):
        # Определяем столбцы для разных сервисов
        columns = {
            'products': [
                {'field': 'id', 'label': 'ID', 'sortable': True},
                {'field': 'name', 'label': 'Name', 'sortable': True},
                {'field': 'price', 'label': 'Price', 'sortable': True},
                {'field': 'quantity', 'label': 'Quantity', 'sortable': True},
            ],
            'orders': [
                {'field': 'id', 'label': 'ID', 'sortable': True},
                {'field': 'customer_name', 'label': 'Customer', 'sortable': True},
                {'field': 'total_amount', 'label': 'Total', 'sortable': True},
                {'field': 'status', 'label': 'Status', 'sortable': True},
            ]
        }
        return columns.get(service_name, [])