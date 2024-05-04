from django.urls import path

from svc.views.purchase_order import (
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
)

purchase_order_urlpatterns = [
    path("purchase-orders", PurchaseOrderListCreateView.as_view()),
    path("purchase-order/<int:pk>", PurchaseOrderRetrieveUpdateDeleteView.as_view()),
]
