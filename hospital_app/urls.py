from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('patients/', PatientListAPIView.as_view(), name='patients_list'),
    path('appointments/', AppointmentListAPIView.as_view(), name='appointments_list'),
    path('appointment/<int:pk>/', AppointmentDetailAPIView.as_view(), name='appointment_detail'),
    path('feedbacks/', FeedbackListAPIView.as_view(), name='feedbacks_list'),
    path('feedback_create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),
    path('feedback/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback_detail'),
    path('doctors/', DoctorListAPIView.as_view(), name='doctors_list'),
    path('doctor/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_profile_detail'),
]

