from django.contrib import admin

from svc.models import Vendor, PurchaseOrder, HistoricalPerformance

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)
