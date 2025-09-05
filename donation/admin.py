from django.contrib import admin
from .models import Donation

# Register your models here.

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "donor", "blood_request", "status", "donated_at")
    list_filter = ("status", "donated_at")
    search_fields = ("donor__email", "blood_request__hospital_address")