from django.db import models
from appointments.models import Appointment

class Prescription(models.Model):

    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)

    medicine = models.TextField()
    dosage = models.CharField(max_length=100)
    notes = models.TextField()