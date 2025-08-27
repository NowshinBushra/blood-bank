from django.db import models
from users.models import User
from blood_request.models import BloodRequest
# Create your models here.

class Donation(models.Model):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    DONATED = 'Donated'
    CANCELED = 'Canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (DONATED, 'Donated'),
        (CANCELED, 'Canceled'),
    ]
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donation")
    blood_request = models.ForeignKey(BloodRequest, on_delete=models.CASCADE, related_name="donation")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    
    donated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation by {self.donor.email} for {self.blood_request.blood_group} ({self.status})"