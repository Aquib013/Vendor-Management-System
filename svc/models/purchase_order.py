from datetime import datetime, timedelta

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from svc.models.vendor import Vendor
from .base import BaseModal
from .historical_performance import HistoricalPerformance

ORDER_STATUS = (
    (0, "Pending"),
    (1, "Completed"),
    (2, "Cancelled"),
)


class PurchaseOrder(BaseModal):
    po_number = models.CharField(unique=True, editable=False)
    vendor = models.ForeignKey(
        Vendor, related_name="purchase_orders", on_delete=models.CASCADE
    )
    order_date = models.DateTimeField(
        auto_now_add=True, help_text="Datetime when the order was placed"
    )
    delivery_date = models.DateTimeField(
        help_text="Expected or actual delivery date of the order"
    )
    items = models.JSONField()
    quantity = models.IntegerField(help_text="Total quantity of items in the PO")
    status = models.CharField(
        choices=ORDER_STATUS, default=0, help_text="Current status of the PO"
    )
    quality_rating = models.FloatField(
        blank=True, null=True, help_text="Rating given to the vendor for this PO"
    )
    issue_date = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when the PO was issued to the vendor"
    )
    acknowledgment_date = models.DateTimeField(
        blank=True, null=True, help_text="Timestamp when the vendor acknowledged the PO"
    )

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"

    @staticmethod
    def get_unique_po_number():
        date = datetime.now().date()
        last_po = PurchaseOrder.objects.filter().order_by("-order_date").first()
        if last_po is None:
            last_po_id = 0
        else:
            last_po_id = last_po.id
        counter = last_po_id + 1
        return f"PO_{date}_{counter}"


@receiver(pre_save, sender=PurchaseOrder)
def purchase_order_pre_save_receiver(sender, instance, **kwargs):
    if instance.pk is None:
        instance.po_number = instance.get_unique_po_number()
        instance.quantity = sum([item["quantity"] for item in instance.items])
        instance.delivery_date = datetime.now().date() + timedelta(days=7)
    else:
        if instance.status == 1:
            instance.acknowledgment_date = datetime.now()


@receiver(post_save, sender=PurchaseOrder)
def purchase_order_post_save_receiver(sender, instance, created, **kwargs):
    if not created:
        vendor = instance.vendor
        if instance.status == 1:
            # Calculated each time a PO status changes to 'completed'.
            on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
            vendor.on_time_delivery_rate = on_time_delivery_rate
        else:
            on_time_delivery_rate = 0

        if instance.status == 1 and instance.quality_rating is not None:
            # Updated upon the completion of each PO where a quality_rating is provided.
            quality_rating_avg = vendor.calculate_avg_quality_ratings()
            vendor.quality_rating_avg = quality_rating_avg
        else:
            quality_rating_avg = 0

        if instance.status == 1:
            average_response_time = vendor.calculate_avg_response_time()
            vendor.average_response_time = average_response_time
        else:
            average_response_time = 0

        fulfillment_rate = vendor.calculate_fulfillment_rate()
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()
        HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_average=quality_rating_avg,
            fulfillment_rate=fulfillment_rate,
            average_response_time=average_response_time,
        )
