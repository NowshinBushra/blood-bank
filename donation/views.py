from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from donation.models import Donation
from donation.serializers import DonationSerializer

# Create your views here.

class DonationViewSet(ModelViewSet):
    
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    # def perform_create(self, serializer):
    #     """Automatically assign logged-in user as donor."""
    #     serializer.save(donor=self.request.user)

    # def get_queryset(self):
    #     """Users can only see their own donations."""
    #     return Donation.objects.filter(donor=self.request.user)