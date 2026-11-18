from django.db import models
from AccountApp.models import Doctor, Patient
# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(upload_to="prescriptions/", blank=True)
    appointment_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        CONFIRMED = "CONFIRMED", "Confirmé"
        CANCELLED = "CANCELLED", "Annulé"
    status = models.CharField(max_length=9, choices=Status.choices,default=Status.PENDING)
    doctor = models.ForeignKey("AccountApp.Doctor", on_delete=models.CASCADE , related_name='appointments')
    patient = models.ForeignKey("AccountApp.Patient", on_delete=models.CASCADE , related_name='appointments')