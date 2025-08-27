from django.shortcuts import render
from blood_request.models import BloodRequest
from blood_request.serializers import BloodRequestSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from blood_request.filters import BloodRequestFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from blood_request.paginations import DefaultPagination
# from api.permissions import IsAdminOrReadOnly
# from product.permissions import IsReviewAuthorOrReadonly
# from drf_yasg.utils import swagger_auto_schema


class BloodRequestViewSet(ModelViewSet):
    
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BloodRequestFilter
    search_fields = ['blood_group']
    pagination_class = DefaultPagination
    # permission_classes = [IsAdminOrReadOnly]

    # @swagger_auto_schema(
    #     operation_summary='Retrive a list of products'
    # )
    # def list(self, request, *args, **kwargs):
    #     """Retrive all the products"""
    #     return super().list(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     operation_summary="Create a product by admin",
    #     operation_description="This allow an admin to create a product",
    #     request_body=ProductSerializer,
    #     responses={
    #         201: ProductSerializer,
    #         400: "Bad Request"
    #     }
    # )
    def perform_create(self, serializer):
        """Only authenticated user can create blood request"""
        serializer.save(user=self.request.user)

    # def create(self, request, *args, **kwargs):
    #     """Only authenticated admin can create product"""
    #     return super().create(request, *args, **kwargs)