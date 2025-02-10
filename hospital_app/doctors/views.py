from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from patients.models import Patient

@api_view(['GET', 'POST', 'DELETE'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        doctors_serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(doctors_serializer.data, safe=False)

    elif request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Doctor.objects.all().delete()
        return JsonResponse(
            {'message': f'{count[0]} Doctors were deleted successfully!'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return JsonResponse({'message': 'The doctor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        doctor_serializer = DoctorSerializer(doctor)
        return JsonResponse(doctor_serializer.data)

    elif request.method == 'PUT':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(doctor, data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data)
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return JsonResponse({'message': 'Doctor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# New view to link patients to a doctor (ManyToMany relationship)
@api_view(['POST'])
def link_patients_to_doctor(request, doctor_id):
    """
    Link one or more patients to a doctor.
    URL: /api/doctors/<doctor_id>/link_patients/
    Payload: {"patient_ids": [1, 2, 3]}
    """
    doctor = get_object_or_404(Doctor, id=doctor_id)

    # Get the patient_ids from the request body
    patient_ids = request.data.get('patient_ids', [])

    if not patient_ids:
        return JsonResponse(
            {"error": "patient_ids list is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Fetch patients from the provided patient_ids
    patients = Patient.objects.filter(id__in=patient_ids)
    if not patients.exists():
        return JsonResponse(
            {"error": "No valid patients found for the provided IDs"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Link patients to the doctor
    doctor.patients.add(*patients)

    return JsonResponse(
        {"message": f"Patients {patient_ids} successfully linked to Doctor {doctor_id}"},
        status=status.HTTP_200_OK
    )