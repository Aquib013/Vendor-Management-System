from rest_framework import authentication
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from svc.models import Vendor
from svc.serializers import VendorSerializer


class VendorListCreateView(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceMetrics(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)
        return Response(vendor.performance_metrics)
