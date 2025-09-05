from rest_framework import serializers
from blood_request.models import BloodRequest
from django.contrib.auth import get_user_model
from users.models import User


class RequesterMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "phone_number"]


class BloodRequestSerializer(serializers.ModelSerializer):
    user = RequesterMiniSerializer(read_only=True)

    class Meta:
        model = BloodRequest
        fields = ['id', 'user', 'blood_group', 'volume', 'hospital_address',
                  'donation_date', 'description', 'status', 'created_at', 'updated_at']  
        read_only_fields = ["id", 'user', 'user_phone', "created_at", "updated_at" 'status',]
        

class BloodRequestListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name")
    user_phone = serializers.CharField(source="user.phone_number")
    user_email = serializers.CharField(source="user.email")

    class Meta:
        model = BloodRequest
        fields = ["user_name", "user_phone", "user_email", "blood_group", 'volume', 'hospital_address',
                  'donation_date', 'status', 'description', "created_at"]
        read_only_fields = ["user_name", "created_at"]
