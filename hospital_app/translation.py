from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class DoctorTranslationOptions(TranslationOptions):
    fields = ('specialty', 'department')

@register(Patient)
class PatientTranslationOptions(TranslationOptions):
    fields = ('blood_type',)


@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)