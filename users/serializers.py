from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    user_image = serializers.ImageField(required=False, allow_null=True)
    blood_group = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    re_password = serializers.CharField(write_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 're_password', 'name', 'blood_group', 'user_image', 'address',
                   'phone_number', 'age', 'last_donation_date', 'is_available']


class UserSerializer(BaseUserSerializer):
    user_image = serializers.ImageField(required=False, allow_null=True)

    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = ['id', 'email', 'name', 'blood_group', 'user_image', 'address',
                   'phone_number', 'age', 'last_donation_date', 'is_available']


class DonorSerializer(serializers.ModelSerializer):
    user_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "phone_number",
                   "blood_group", 'user_image', "last_donation_date", "is_available"]