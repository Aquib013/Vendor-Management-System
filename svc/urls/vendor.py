from django.urls import path

from svc.views.vendor import VendorListCreateView, VendorRetrieveUpdateDeleteView

vendor_urlpatterns = [
    path("vendors", VendorListCreateView.as_view()),
    path("vendor/<int:pk>", VendorRetrieveUpdateDeleteView.as_view()),
]
