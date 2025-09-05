from django_filters.rest_framework import FilterSet
from users.models import User


class DonorFilter(FilterSet):
    class Meta:
        model = User
        fields = {
            'blood_group': ['exact'],
            'is_available': ['exact'],
        }