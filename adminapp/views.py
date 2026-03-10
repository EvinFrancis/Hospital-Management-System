from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login
from django.contrib import messages

from django.contrib.auth.models import User
from adminapp.models import *



# Create your views here.
def admin_page(request):
    # doctors = Doctor.objects.count()
    # patients = Patient.objects.count()
    # appointments = Appointment.objects.count()

    return render(request, 'index.html')

def admin_loginpage(request):
    return render(request, 'admin_login_page.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        


    if User.objects.filter(username__contains=username).exists():

        user=authenticate(request, username=username, password=password)
        if user is not None and  user:
            login(request, user)
            request.session['username'] = username
            request.session['password'] = password
            messages.success(request, "Login successful")
            return redirect(admin_page)

            
        else:
            messages.error(request, "Invalid login credentials")
            return redirect(admin_loginpage)
        
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)


# doctor page

def view_doctors(request):
    return render(request,'Doctor_section.html')

#svae doctors




#view department

def view_departments(request):
    return render(request,'department_section.html')
             

#save deparrtment

def save_department(request):

    if request.method == "POST":

        dpt_name = request.POST.get('dpt_name')
        dpt_des = request.POST.get('dpt_des')
        dpt_phone = request.POST.get('dpt_phone')
        dpt_email = request.POST.get('dpt_email')
        dpt_image = request.FILES.get('dpt_image')

        departmentdb.objects.create(
            dpt_name=dpt_name,
            dpt_des=dpt_des,
            dpt_phone=dpt_phone,
            dpt_email=dpt_email,
            dpt_image=dpt_image
        )

        messages.success(request, "Department Added Successfully ✅")

        return redirect(view_departments)
       

