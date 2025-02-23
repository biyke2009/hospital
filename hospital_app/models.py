from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                       MaxValueValidator(100)],
                                           null=True,blank=True)
    DAYS_CHOICES =(
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=15,choices=DAYS_CHOICES, default='patient')
    phone_number=PhoneNumberField(null=True,blank=True)
    profile_picture = models.ImageField( null=True,blank=True)


    def __str__(self):
          return f'{self.first_name}-{self.last_name}'


class Doctor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=65)
    department = models.CharField(max_length=65)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    DAY_CHOICES =(
        ('ПН','ПН'),
        ('ВТ','ВТ'),
        ('СР','СР'),
        ('ЧТ','ЧТ'),
        ('ПТ','ПТ'),
        ('СР','СР'),
    )
    working_days = models.CharField(max_length=32, choices=DAY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user}'


class Patient(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name='patient_profile')
    emergency_contact= models.CharField(max_length=65, null=True,blank=True)
    BLOOD_CHOICES = (
        ('I+','I+'),
        ('I-','I-'),
        ('II+','II+'),
        ('II-','II-'),
        ('III+','III+'),
        ('III-','III-'),
        ('IV+','IV+'),
        ('IV-','IV-'),
    )

    blood_type= models.CharField(max_length=4, choices=BLOOD_CHOICES, null=True,blank=True)

    def __str__(self):
        return f'{self.user}'


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('запланировано', 'Запланировано'),
        ('завершено', 'Завершено'),
        ('отменено', 'Отменено'),
    )
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE, related_name='appointment')
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name='appointment')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20,default='запланировано')

    def __str__(self):
        return f'{self.patient}-{self.doctor}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient}-{self.doctor}'

class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name='feedbacks')
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='feedbacks')
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient}-{self.doctor}-{self.rating}'


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)