from django.urls import path, include
from blood_request.views import BloodRequestViewSet
from donation.views import DonationViewSet
from users.views import DonorViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('blood_requests', BloodRequestViewSet, basename='blood_requests')
router.register('donations', DonationViewSet, basename='donations')
router.register('donors', DonorViewSet, basename='donors')


urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
]
