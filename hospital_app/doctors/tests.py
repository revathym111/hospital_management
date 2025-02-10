import pytest
from django.test import TestCase
from doctors.models import Doctor
from patients.models import Patient

# Create your tests here.
def test_doctor_initialization():
    doctor = Doctor(name="Dr.John Smith", specialization="Cardiology")

    assert doctor.name == "Dr.John Smith"
    assert doctor.specialization == "Cardiology"

@pytest.mark.django_db
def test_create_doctor():
    doctor = Doctor.objects.create(
        name='Dr.Jack Russell',
        specialization='Pediatrics',
        contact_number='2134567890',
        email_id='jack@example.com'
    )
    assert doctor.specialization == "Pediatrics"