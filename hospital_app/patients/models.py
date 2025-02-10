from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=70, blank=False)
    date_of_birth = models.DateField(blank=False)
    gender = models.CharField(max_length=14, blank=False)
    contact_number = models.PositiveIntegerField()
    email_id = models.EmailField(max_length=255, blank=False)
   