from django.db import models

# Create your models here.
class appointmentdb(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    department = models.TextField(max_length=100)
    doctor = models.TextField(max_length=100)

    date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name