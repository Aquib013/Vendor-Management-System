from django.urls import path

from svc.views.purchase_order import (
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    AcknowledgePurchaseOrder,
)

purchase_order_urlpatterns = [
    path("purchase_orders", PurchaseOrderListCreateView.as_view()),
    path("purchase_orders/<int:pk>", PurchaseOrderRetrieveUpdateDeleteView.as_view()),
    path(
        "purchase_orders/<int:pk>/acknowledge",
        AcknowledgePurchaseOrder.as_view(),
    ),
]
