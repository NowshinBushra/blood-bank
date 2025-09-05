
from rest_framework import serializers
from donation.models import Donation
from users.models import User
from blood_request.models import BloodRequest


class EmptySerializer(serializers.Serializer):
    pass

class SimpleDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "phone_number", "blood_group"]

class SimpleBloodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodRequest
        fields = ["id", "blood_group"]


class DonationSerializer(serializers.ModelSerializer):
    donor = SimpleDonorSerializer(read_only=True)
    blood_request = SimpleBloodRequestSerializer(read_only=True)

    class Meta:
        model = Donation
        fields = ['id', 'donor', 'blood_request', 'status', 'donated_at', 'updated_at']  
        read_only_fields = ["id", 'donor', "blood_request", "donated_at", "updated_at"]


class CreateDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["blood_request"]
        def validate(self, attrs):
            if attrs["blood_request"].user_id == self.context["request"].user.id:
                raise serializers.ValidationError("You cannot accept your own request.")
            return attrs
        
    
class UpdateDonationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["status"]
