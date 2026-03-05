from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending','Pending'),
            ('approved','Approved'),
            ('completed','Completed')
        ]
    )