from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from svc.models.vendor import Vendor

ORDER_STATUS = (
    ("pending", "pending"),
    ("completed", "completed"),
    ("cancelled", "cancelled"),
)


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=ORDER_STATUS)
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgement_date = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.po_number

    @staticmethod
    def get_unique_po_no():
        latest_po_id = PurchaseOrder.objects.filter().order_by("-pk").first().id
        new_po = int(latest_po_id) + 1
        today = datetime.now().strftime("%Y%m%d")
        return f"{today}-{new_po}"


@receiver(pre_save, sender=PurchaseOrder)
def purchase_order_pre_save_receiver(sender, instance, **kwargs):
    instance.quantity = sum([item["quantity"] for item in instance.items])
    if instance.pk is None:
        instance.po_number = instance.get_unique_po_no()
    if instance.status == "completed":
        instance.delivery_date = datetime.now()


@receiver(post_save, sender=PurchaseOrder)
def purchase_order_post_save_receiver(sender, instance, created, **kwargs):
    if not created and instance.status == "completed":

        completed_pos = PurchaseOrder.objects.filter(
            vendor=instance.vendor, status="completed"
        )
        on_time_deliveries = completed_pos.filter(
            delivery_date__lte=instance.completed_date
        ).count()
        total_completed_pos = completed_pos.count()
        if total_completed_pos > 0:
            instance.on_time_delivery_rate = on_time_deliveries / total_completed_pos
        else:
            instance.on_time_delivery_rate = 0.0
