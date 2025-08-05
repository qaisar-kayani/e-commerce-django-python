from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        instance.save()
        return instance

