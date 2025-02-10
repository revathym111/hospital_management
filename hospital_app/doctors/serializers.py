from rest_framework import serializers
from doctors.models import Doctor
from patients.models import Patient  
from patients.serializers import PatientSerializer


class DoctorSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id','name', 'specialization', 'contact_number', 'email_id', 'patients')
