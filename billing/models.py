from django.db import models
from appointments.models import Appointment

class Bill(models.Model):

    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)

    consultation_fee = models.DecimalField(max_digits=8,decimal_places=2)

    test_charges = models.DecimalField(max_digits=8,decimal_places=2)

    payment_status = models.CharField(max_length=20)