from django.urls import path
from doctors import views as doctors_views
from django.conf.urls.static import static
from django.conf import settings

'''urlpatterns = [
    #path('', doctors_views.index, name='home'),
    path('', doctors_views.index.as_view(), name='home'),
    path('api/doctors/', doctors_views.doctor_list),
    path('api/doctors/<int:pk>/', doctors_views.doctor_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''


urlpatterns = [
    #path('', doctors_views.index.as_view(), name='home'),
    path('api/doctors/', doctors_views.doctor_list, name='doctor_list'),
    path('api/doctors/<int:pk>/', doctors_views.doctor_detail, name='doctor_detail'),
    path('api/doctors/<int:doctor_id>/link_patients/', doctors_views.link_patients_to_doctor, name='link_patients_to_doctor'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
