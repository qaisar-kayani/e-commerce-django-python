from rest_framework import serializers
from .models import Users

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if Users.objects(email=value).first():
            raise serializers.ValidationError("Email is already in use.")
        return value

    def validate_username(self, value):
        if Users.objects(username=value).first():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def create(self, validated_data):
        user = Users(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = Users.objects.get(email=data['email'])
        except Users.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Incorrect password")

        return user
