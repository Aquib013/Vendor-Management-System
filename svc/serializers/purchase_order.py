from rest_framework import serializers

from svc.models.purchase_order import PurchaseOrder


class PurchaseOrderItemSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        extra_kwargs = {
            "quantity": {"required": False},
            "po_number": {"required": False},
        }
        items = serializers.ListField(
            child=PurchaseOrderItemSerializer(required=True), required=True
        )

    def validate(self, data):
        items = data["items"]
        if len(items) == 0:
            raise serializers.ValidationError({"items": "Please add at least one item"})
        status = data["status"]
        quality_rating = data["quality_rating"]
        if status == "completed" and quality_rating is None:
            raise serializers.ValidationError(
                {"quality_rating": "Quality rating cannot be empty"}
            )
        return data
