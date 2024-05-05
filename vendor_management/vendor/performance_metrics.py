# performance_metrics.py

from django.db.models import Avg, Count
from .models import PurchaseOrder,Vendor
from django.utils import timezone
from django.db.models import F

def calculate_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_pos = completed_pos.filter(delivery_date__lte=timezone.now())
    if completed_pos.exists():
        return on_time_pos.count() / completed_pos.count()
        
    else:
        return 0

def calculate_quality_rating_average(vendor):
    return PurchaseOrder.objects.filter(vendor=vendor, status='completed').aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

def calculate_average_response_time(vendor):
    return PurchaseOrder.objects.filter(vendor=vendor, status='completed').aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time'] or 0

def calculate_fulfillment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    successful_pos = total_pos.filter(status='completed')
    if total_pos.exists():
        return successful_pos.count() / total_pos.count()

    else:
        return 0
