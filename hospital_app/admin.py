from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Doctor, Feedback)
class DoctorAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class AppointmentsInline(admin.TabularInline):
    model = Appointment
    extra = 1


@admin.register(Patient)
class PatientAdmin(TranslationAdmin):
    inlines = [AppointmentsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




admin.site.register(UserProfile)
admin.site.register(Chat)
admin.site.register(Message)
