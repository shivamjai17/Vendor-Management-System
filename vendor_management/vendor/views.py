# views.py

from rest_framework import viewsets
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .performance_metrics import *

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            'name': instance.name,
            'on_time_delivery_rate': calculate_on_time_delivery_rate(instance),
            'quality_rating_avg': calculate_quality_rating_average(instance),
            'average_response_time': calculate_average_response_time(instance),
            'fulfillment_rate': calculate_fulfillment_rate(instance),

        }
        return Response(data, status=status.HTTP_200_OK)    
