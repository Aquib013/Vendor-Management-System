from rest_framework import serializers

from svc.models.historical_performance import HistoricalPerformance


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    model = HistoricalPerformance
    fields = "__all__"
