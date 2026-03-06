from django.shortcuts import render,redirect
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.
def admin_page(request):
    doctors = Doctor.objects.count()
    patients = Patient.objects.count()
    appointments = Appointment.objects.count()

    return render(request, 'index.html',{
        "doctors": doctors,
        "patients": patients,
        "appointments": appointments
    }
)

def admin_loginpage(request):
    return render(request, 'admin_login_page.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    if User.objects.filter(username__contains=username).exists():

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session['password'] = password
            return redirect(admin_page)
        else:
            return render(request, 'index.html', {
                'error': 'Invalid username or password'
            })
             
        return render(request, 'index.html', {
            'username': username,
            'password': password
        })
    

