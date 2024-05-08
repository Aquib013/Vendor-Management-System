import json

from rest_framework import generics, authentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from svc.models import PurchaseOrder
from svc.serializers import PurchaseOrderSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    allowed_params = ["vendor_id"]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_filter = dict()
        for param in self.allowed_params:
            if self.request.GET.get(param, None) is not None:
                query_filter[param] = self.request.GET[param]
        return queryset.filter(**query_filter)


class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]


class AcknowledgePurchaseOrder(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    allowed_payload = ["quality_rating"]

    def post(self, request, pk):
        po = get_object_or_404(PurchaseOrder, pk=pk)
        payload = json.loads(request.body)
        for k, v in payload.items():
            if k in self.allowed_payload:
                setattr(po, k, v)
        po.status = 1
        po.save()
        return Response(data="Purchase Order updated successfully.")
