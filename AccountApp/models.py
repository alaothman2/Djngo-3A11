from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
# Create your models here.
class User(AbstractUser):
    pass 

class Specialty(models.Model):
    name = models.CharField(max_length=100)

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True , validators=[MinLengthValidator(6)] )
    phone = models.CharField(max_length=8)
    specialties = models.ManyToManyField(Specialty ,related_name='doctors')
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True , validators=[MinLengthValidator(8), RegexValidator(regex=r'^[0-9]{8}$')]  )
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()
