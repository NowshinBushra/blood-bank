from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from users.models import User
from users.serializers import DonorSerializer

# Create your views here.


class DonorViewSet(ReadOnlyModelViewSet):
    serializer_class = DonorSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_available=True)  
        blood_group = self.request.query_params.get('blood_group')  
        if blood_group:
            queryset = queryset.filter(blood_group=blood_group)
        return queryset