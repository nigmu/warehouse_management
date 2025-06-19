from rest_framework import serializers
from .models import Stack

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

    # This handles validation to ensure that the block belongs to the selected warehouse
    def validate(self, data):
        block = data.get('block')
        warehouse = data.get('warehouse')
        if block.warehouse != warehouse:
            raise serializers.ValidationError(f"The selected block ({block.block_name}) does not belong to the selected warehouse ({warehouse.warehouse_name}).")

        return data