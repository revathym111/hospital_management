from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Patient.objects.all()
    return render(request, "patients/index.html", {'patients': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'patients/index.html'

    def get(self, request):
        queryset = Patient.objects.all()
        return Response({'patients': queryset})


class list_all_patients(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'patients/patient_list.html'

    def get(self, request):
        queryset = Patient.objects.all()
        return Response({'patients': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()

        '''title = request.GET.get('title', None)
        if title is not None:
            patients = patients.filter(title__icontains=title)'''

        patients_serializer = PatientSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(patient_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Patient.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Patients were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return JsonResponse({'message': 'The patient does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        patient_serializer = PatientSerializer(patient)
        return JsonResponse(patient_serializer.data)

    elif request.method == 'PUT':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data)
        return JsonResponse(patient_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return JsonResponse({'message': 'Patient was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


'''@api_view(['GET'])
def patient_list_published(request):
    patients = Patient.objects.filter(published=True)

    if request.method == 'GET':
        patients_serializer = PatientSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)'''

'''api_view(['GET'])
def doctor_list(request):
    # Assuming you have a field to distinguish doctors, e.g., `is_doctor` in `Patient`
    doctors = Patient.objects.filter(is_doctor=True)
    doctor_serializer = PatientSerializer(doctors, many=True)
    return JsonResponse(doctor_serializer.data, safe=False)'''
