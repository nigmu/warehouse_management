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


# Serializer for searching stock by tile name, tile size, warehouse, block, and quantity
class StockSearchSerializer(serializers.Serializer):
    tile_name = serializers.CharField(source='tile.tile_name')
    size = serializers.CharField(source='tile.size')
    warehouse = serializers.CharField(source='block.warehouse.warehouse_name')
    block = serializers.CharField(source='block.block_name')
    quantity = serializers.IntegerField()
