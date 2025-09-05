from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from donation.models import Donation
from donation.serializers import EmptySerializer, DonationSerializer, CreateDonationSerializer, UpdateDonationStatusSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class DonationViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch', 'head', 'options']
    permission_classes = [IsAuthenticated]


    @swagger_auto_schema(
        operation_summary='Retrive a list of donations',
        responses={200: DonationSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """Retrive all the donation history"""
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a donation by user",
        operation_description="This allows an authenticated user to accept and create a donation",
        request_body=DonationSerializer,
        responses={
            201: DonationSerializer,
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """A user can cancel the donation of a blood request"""
        donation  = self.get_object()
        if donation.donor != request.user and not request.user.is_staff:
            return Response({"error": "Not allowed"}, status=403)
        donation.status = Donation.CANCELED
        donation.save()
        return Response({'status': 'Donation canceled'})
    
    
    @action(detail=False, methods=['get'])
    def my_donations(self, request):
        """Lists all donations donated by the logged-in user"""
        qs = Donation.objects.select_related("donor", "blood_request").filter(donor=request.user)
        serializer = DonationSerializer(qs, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def update_status(self, request, pk=None):
        """Only authenticated users can updated their donation status to Pending/Accepted/Donated/Cancelled"""
        donation = self.get_object()
        serializer = UpdateDonationStatusSerializer(
            donation, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': f'Donation status updated to {request.data["status"]}'})
    

    def get_permissions(self):
        if self.action in ['destroy']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        qs = Donation.objects.select_related("donor", "blood_request")
        if not self.request.user.is_authenticated:
            return qs.none()
        if self.request.user.is_staff:
            return qs
        return qs.filter(donor=self.request.user)


    def get_serializer_class(self):
        if self.action == 'cancel':
            return EmptySerializer
        if self.action == "create":
            return CreateDonationSerializer
        elif self.action in ["update", "partial_update"]:
            return UpdateDonationStatusSerializer
        return DonationSerializer


    def perform_create(self, serializer):
        """Automatically assign logged-in user as donor."""
        serializer.save(donor=self.request.user)

    # def get_serializer_context(self):
        # if getattr(self, 'swagger_fake_view', False):
        #     return super().get_serializer_context()
        # return {'user_id': self.request.user.id, 'user': self.request.user}