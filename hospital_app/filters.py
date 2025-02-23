from django_filters.rest_framework import FilterSet
from .models import Doctor


class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'price': ['gt', 'lt'],
            'department': ['exact'],
            'specialty': ['exact'],
            'working_days': ['exact']
        }