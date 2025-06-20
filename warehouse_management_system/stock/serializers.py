from rest_framework import serializers
from .models import Stack

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

    def validate(self, data):
        block = data.get('block')
        warehouse = data.get('warehouse')
        tile = data.get('tile')
        quantity = data.get('quantity')

        if block.warehouse != warehouse:
            raise serializers.ValidationError(
                f"The selected block ({block.block_name}) does not belong to the selected warehouse ({warehouse.warehouse_name})."
            )

        if quantity is not None and quantity < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        
        if tile is None:
            raise serializers.ValidationError("Tile must be selected.")

        return data
