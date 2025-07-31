from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp.core.api import TableDataAPIView

# Сервис A
from erp.services.service_a.views import ProductViewSet

# Сервис B
from erp.services.service_b.views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/table/<str:service_name>/', TableDataAPIView.as_view(), name='table-data'),
]