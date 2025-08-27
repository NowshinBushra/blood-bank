from django_filters.rest_framework import FilterSet
from blood_request.models import BloodRequest


class BloodRequestFilter(FilterSet):
    class Meta:
        model = BloodRequest
        fields = {
            'blood_group': ['exact'],
            'donation_date': ['exact', 'year__gt'],
        }