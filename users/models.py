from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from cloudinary.models import CloudinaryField
# Create your models here.

class User(AbstractUser):
    BLOOD_GROUP_CHOICES=[
        ("A+", "A+"), ("A-", "A-"),
        ("B+", "B+"), ("B-", "B-"),
        ("O+", "O+"), ("O-", "O-"),
        ("AB+", "AB+"), ("AB-", "AB-"),
    ]

    username = None
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    # profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True)
    user_image = CloudinaryField('user_image')

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    