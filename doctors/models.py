from django.db import models
from accounts.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)# related_name='doctors')
#     3️⃣ on_delete=models.CASCADE

# This defines what happens when the referenced department is deleted.

# CASCADE means:

# ➡ If a Department is deleted, all Doctors in that department will also be deleted automatically.
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username