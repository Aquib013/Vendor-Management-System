from django.db import models

from .base import BaseModal


class Vendor(BaseModal):
    name = models.CharField()
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

    @property
    def performance_metrics(self):
        return dict(
            on_time_delivery_rate=self.on_time_delivery_rate,
            quality_rating_avg=self.quality_rating_avg,
            average_response_time=self.average_response_time,
            fulfillment_rate=self.fulfillment_rate,
        )

    def calculate_on_time_delivery_rate(self) -> float:
        completed_pos = self.purchase_orders.filter(status=1)  # NOQA
        pos_delivered_on_or_before_delivery_date = completed_pos.filter(
            acknowledgment_date__lte=models.F("delivery_date")
        )
        try:
            percentage = round(
                (
                    pos_delivered_on_or_before_delivery_date.count()
                    / completed_pos.count()
                )
                * 100,
                2,
            )
            return percentage

        except ZeroDivisionError:
            return 0

    def calculate_avg_quality_ratings(self):
        """
        The function calculates the average quality rating of completed purchase orders
        """
        completed_pos = self.purchase_orders.filter(status=1)  # NOQA
        result = completed_pos.aggregate(
            avg_quality_rating=models.Avg("quality_rating", default=0.0)
        )
        return round(result.get("avg_quality_rating"))

    def calculate_fulfillment_rate(self):
        """
        The function calculates the fulfillment rate by dividing the number of completed purchase orders
        by the total number of purchase orders
        """
        completed_pos = self.purchase_orders.filter(status=1)  # NOQA
        total_pos = self.purchase_orders.all()  # NOQA
        try:
            return round((completed_pos.count() / total_pos.count()) * 100, 2)

        except ZeroDivisionError:
            return 0

    def calculate_avg_response_time(self):
        """
        The function calculates the average response time for purchase orders that have both an issue
        date and an acknowledgment date
        """
        filter_po_data = self.purchase_orders.filter(  # NOQA
            issue_date__isnull=False, acknowledgment_date__isnull=False
        )
        if filter_po_data.exists():
            result = filter_po_data.aggregate(
                avg_response_time=models.Avg(
                    models.F("acknowledgment_date") - models.F("issue_date")
                )
            )
            avg_response_time_in_seconds = result.get(
                "avg_response_time"
            ).total_seconds()
            avg_response_time_in_days = avg_response_time_in_seconds / (60 * 60 * 24)
            return round(avg_response_time_in_days, 2)
        return 0
