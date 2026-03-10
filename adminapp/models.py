from django.db import models



# Create your models here.
# department db
class departmentdb(models.Model):
    dpt_name = models.CharField(max_length=100)
    dpt_des = models.TextField(max_length=1000)
    dpt_phone=models.TextField(max_length=100)
    dpt_email=models.EmailField(max_length=100)

    dpt_image = models.ImageField(upload_to='departments/', blank=True, null=True)

    def __str__(self):
        return self.name

