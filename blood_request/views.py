from django.shortcuts import render
from blood_request.models import BloodRequest
from blood_request.serializers import BloodRequestSerializer, BloodRequestListSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from blood_request.filters import BloodRequestFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from blood_request.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from blood_request.permissions import IsRequestRecipientOrReadonly
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class BloodRequestViewSet(ModelViewSet):
    
    queryset = BloodRequest.objects.select_related("user").all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BloodRequestFilter
    search_fields = ['blood_group']
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BloodRequestListSerializer 
        return BloodRequestSerializer 
    
    @swagger_auto_schema(
        operation_summary='Retrive a list of blood-requests',
        responses={200: BloodRequestListSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the blood-requests"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a blood request by user",
        operation_description="This allows an authenticated user to create a blood-request",
        request_body=BloodRequestSerializer,
        responses={
            201: BloodRequestSerializer,
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        """Only authenticated user can create blood request"""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Only authenticated users can update their created blood request"""
        serializer.save(user=self.request.user)


    @action(detail=False, methods=['get'])
    def my_requests(self, request):
        """List blood-requests created by the logged-in user"""
        rqs = (BloodRequest.objects
                .select_related("user")
                .prefetch_related("donation__donor")
                .filter(user=request.user))
        serializer = BloodRequestSerializer(rqs, many=True)
        return Response(serializer.data)

