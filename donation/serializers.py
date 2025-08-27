
from rest_framework import serializers
from donation.models import Donation


class DonationSerializer(serializers.ModelSerializer):
    donor_email = serializers.EmailField(source="donor.email", read_only=True)
    donor_phone = serializers.CharField(source="donor.phone_number", read_only=True)

    class Meta:
        model = Donation
        fields = ['id', 'donor', 'donor_email', 'donor_phone', 'blood_request', 'status', 'donated_at', 'updated_at']  
        read_only_fields = ["id", 'donor', "donated_at", "updated_at"]