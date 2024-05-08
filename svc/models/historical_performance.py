from django.db import models

from svc.models.vendor import Vendor
from .base import BaseModal


class HistoricalPerformance(BaseModal):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now_add=True, help_text="Date of the performance record"
    )
    on_time_delivery_rate = models.FloatField(
        help_text="Historical record of the on-time delivery rate"
    )
    quality_rating_average = models.FloatField(
        help_text="Historical record of the quality rating average"
    )
    average_response_time = models.FloatField(
        help_text="Historical record of the average response time"
    )
    fulfillment_rate = models.FloatField(
        help_text="Historical record of the fulfilment rate"
    )

    def __str__(self):
        return f"{self.vendor.name} performance data"
