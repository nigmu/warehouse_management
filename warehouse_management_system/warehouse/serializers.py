from rest_framework import serializers
from .models import Warehouse, Block


# Serializers for Warehouse model
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

# Serializers for Block model
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'