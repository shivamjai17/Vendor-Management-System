# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
router.register(r'purchase_orders', views.PurchaseOrderViewSet)
router.register(r'historical_performance', views.HistoricalPerformanceViewSet)

urlpatterns = [
    path('api/vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/', include(router.urls)),

]
