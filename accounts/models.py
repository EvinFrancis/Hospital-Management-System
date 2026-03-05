from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):#inheritance abtractuser for user model

    ROLE_CHOICES = (
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('receptionist','Receptionist'),
        ('patient','Patient'),
    )#choices for role of user model and

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)#role field how many choices are there