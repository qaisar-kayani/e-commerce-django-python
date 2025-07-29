from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name =  serializers.CharField(required = False)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.FloatField()
    category = serializers.CharField(required=False, allow_blank=True)
    brand = serializers.CharField(required=False, allow_blank=True)
    stock = serializers.IntegerField(required=False)
    images = serializers.ListField(child=serializers.CharField(), required=False)
    is_active = serializers.BooleanField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance
