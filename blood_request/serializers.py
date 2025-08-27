from rest_framework import serializers
from blood_request.models import BloodRequest
from django.contrib.auth import get_user_model




class BloodRequestSerializer(serializers.ModelSerializer):
    user_phone = serializers.CharField(source="user.phone_number")

    class Meta:
        model = BloodRequest
        fields = ['id', 'user', 'user_phone', 'blood_group', 'status', 'hospital_address',
                  'donation_date', 'description', 'created_at', 'updated_at']  
        read_only_fields = ["id", 'user', "created_at", "updated_at", "status"]
        
