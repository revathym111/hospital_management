from django.contrib import admin
from .models import Doctor

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'contact_number', 'email_id')  # Customize fields displayed
    search_fields = ('name', 'specialization')  # Enable search functionality
