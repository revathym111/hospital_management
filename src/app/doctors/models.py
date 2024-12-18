from django.db import models
from patients.models import Patient

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=False)
    specialization = models.CharField(max_length=255, blank=False)
    contact_number = models.PositiveIntegerField()
    email_id = models.EmailField(max_length=255, blank=False)
    patients = models.ManyToManyField(Patient, null=True, blank=True)

