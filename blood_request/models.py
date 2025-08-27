from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class BloodRequest(models.Model):
    PENDING = 'Pending'
    CLOSED = 'Closed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CLOSED, 'Closed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blood_request")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    blood_group = models.CharField(max_length=3, choices=User.BLOOD_GROUP_CHOICES)
    volume = models.CharField(max_length=50, help_text="(e.g., 3 bags)")
    donation_date = models.DateField()
    hospital_address  = models.TextField(blank=True, null=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.user.email} for {self.blood_group} ({self.status})"