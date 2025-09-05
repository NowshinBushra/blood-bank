from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from users.models import User
from users.serializers import DonorSerializer, UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from users.filters import DonorFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

# class UserViewSet(ModelViewSet):
#     # queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get_permissions(self):
#         if self.action in ['list', 'destroy']:
#             return [IsAdminUser()]
#         return [IsAuthenticated()]

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff:
#             return User.objects.all()
#         return User.objects.filter(id=user.id)
    



class DonorViewSet(ModelViewSet):
    serializer_class = DonorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DonorFilter
    search_fields = ['blood_group', 'name', 'email', 'phone_number', 'address']


    @swagger_auto_schema(
    operation_summary="Create donors",
    operation_description="This allows an authenticated user to be a donor",
    request_body=UserCreateSerializer,
    responses={
        201: UserCreateSerializer,
        400: "Bad Request"
    }
)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Retrive a list of donors',
        responses={200: DonorSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the donors"""
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.filter(is_available=True)  
        blood_group = self.request.query_params.get('blood_group')  
        if blood_group:
            queryset = queryset.filter(blood_group=blood_group)
        return queryset
    
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
