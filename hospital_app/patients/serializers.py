from rest_framework import serializers
from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('name', 'date_of_birth', 'gender', 'contact_number', 'email_id')
