from django.contrib import admin # Register your models here.
from .models import Doctor, Department# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user", "department", "phone")


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Department)