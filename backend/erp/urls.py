from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp.services.service_a.views import ProductViewSet
from erp.services.service_b.views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
