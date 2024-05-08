from django.urls import path

from svc.views.vendor import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    VendorPerformanceMetrics,
)

vendor_urlpatterns = [
    path("vendors", VendorListCreateView.as_view()),
    path("vendors/<int:pk>", VendorRetrieveUpdateDeleteView.as_view()),
    path("vendors/<int:pk>/performance", VendorPerformanceMetrics.as_view()),
]
