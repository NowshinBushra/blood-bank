from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'name', 'blood_group', 'profile_image', 'address',
                   'phone_number', 'age', 'last_donation_date', 'is_available']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = ['id', 'email', 'name', 'blood_group', 'profile_image', 'address',
                   'phone_number', 'age', 'last_donation_date', 'is_available']


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "phone_number",
                   "blood_group", 'profile_image', "last_donation_date", "is_available"]