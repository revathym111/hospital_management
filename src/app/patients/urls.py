from django.urls import path
from patients import views as patients_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', patients_views.index, name='home'),
    path('', patients_views.index.as_view(), name='home'),
    path('api/patients/', patients_views.patient_list),
    path('api/patients/<int:pk>/', patients_views.patient_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)