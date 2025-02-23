from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'phone_number',]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = 'all'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class DoctorListSerializers(serializers.ModelSerializer):
    user_doctor = UserProfileSimpleSerializers()
    shrift_start = serializers.TimeField(format('%H-%m'))
    shrift_end = serializers.TimeField(format('%H-%m'))
    class Meta:
        model = Doctor
        fields = ['id', 'user_doctor', 'specialty', 'shrift_start','shrift_end',
            'service_prise']


class DoctorDetailSerializers(serializers.ModelSerializer):
    user_doctor = UserProfileSimpleSerializers()
    shrift_start = serializers.TimeField(format('%H-%m'))
    shrift_end = serializers.TimeField(format('%H-%m'))
    class Meta:
        model = Doctor
        fields = ['id', 'user_doctor', 'specialty', 'department', 'work_day',
                  'shrift_start', 'shrift_end','service_prise']


class PatientListSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers(read_only=True)
    class Meta:
        model = Patient
        fields = 'all'


class AppointmentListSerializers(serializers.ModelSerializer):
    patient_app = PatientListSerializers(read_only=True)
    date_time = serializers.DateTimeField(format('%m-%H-%Y'))
    class Meta:
        model = Appointment
        fields = ['id', 'patient_app', 'date_time', 'status']


class AppointmentDetailSerializers(serializers.ModelSerializer):
    patient_app = PatientListSerializers(read_only=True)
    doctor_app = DoctorListSerializers(read_only=True)
    date_time = serializers.DateTimeField(format('%m-%H-%Y'))
    class Meta:
        model = Appointment
        fields = ['patient_app', 'doctor_app', 'date_time', 'status']


class FeedbackListSerializers(serializers.ModelSerializer):
    doctor_feed = DoctorListSerializers(read_only=True)
    patient_feed = PatientListSerializers(read_only=True)
    class Meta:
        model = Feedback
        fields = ['doctor_feed', 'patient_feed', 'rating', 'comment']


class FeedbackDetailSerializers(serializers.ModelSerializer):
    doctor_feed = DoctorListSerializers(read_only=True)
    patient_feed = PatientListSerializers(read_only=True)
    class Meta:
        model = Feedback
        fields = ['doctor_feed', 'patient_feed', 'rating', 'comment']


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['doctor_feed', 'specialty',
                  'department', 'work_day', 'shrift_start','shrift_end',
                  'service_prise', 'patient_feed']


class MedicalRecordListSerializers(serializers.ModelSerializer):
    created_at = serializers.DateField(format='%H-%m  %d-%Y')
    class Meta:
        model = MedicalRecord
        fields = ['id', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class MedicalRecordDetailSerializers(serializers.ModelSerializer):
    patient_record = PatientListSerializers(read_only=True)
    doctor_record = DoctorListSerializers(read_only=True)
    created_at = serializers.DateField(format='%H-%m  %d-%Y')
    class Meta:
        model = MedicalRecord
        fields = ['patient_record', 'doctor_record', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']
