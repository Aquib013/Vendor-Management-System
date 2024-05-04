from django.db import models


class Vendor(models.Model):
    name = models.CharField()
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.name
