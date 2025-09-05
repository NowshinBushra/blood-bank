from django.contrib import admin
from .models import BloodRequest

# Register your models here.

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "blood_group", "status", "hospital_address", "donation_date", "created_at")
    list_filter = ("blood_group", "status", "donation_date")
    search_fields = ("user__email", "hospital_address", "description")