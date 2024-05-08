import json

from rest_framework import serializers

from svc.models.purchase_order import PurchaseOrder


class PurchaseOrderItemSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = ("id", "items", "quantity", "vendor", "status", "quality_rating")
        items = PurchaseOrderItemSerializer(many=True)
        extra_kwargs = {"quantity": {"required": False}}

    def validate(self, data):
        items = data["items"]
        if len(items) == 0:
            raise serializers.ValidationError({"items": "Please add at least one item"})
        for item in items:
            item_serializer = PurchaseOrderItemSerializer(data=item)
            if not item_serializer.is_valid():
                str_dict = json.dumps(item)
                raise serializers.ValidationError(
                    {"items": f"{str_dict} is not a valid item data"}
                )
        return data
