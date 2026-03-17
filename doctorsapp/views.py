from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth import authenticate,login
from django.contrib import messages

from django.contrib.auth.models import User
from adminapp.models import *
from django.core.mail import send_mail
from django.conf import settings
import random



def sigin_page(request):

    return render(request,'sigin_page.html')

#dcoctor section
def  doctor_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=username+"123"
        password=request.POST.get('password')
        if doctordb.objects.filter(doc_name__contains=username).exists():
            otp = random.randint(100000,999999)

            request.session['username'] = username
            request.session['password'] = password
            request.session['otp'] = otp

            if pass1 == password:
                send_mail(
                'Admin Login Alert',
                f'Admin {username} has logged into the Hospital Management System.Admin Login OTP ,\n\n  ---Your OTP for admin login is {otp}',
                settings.EMAIL_HOST_USER,
                ['evinfrancisvastgcsj@gmail.com'],
                fail_silently=False,
            )
            
                return redirect(verify_otp)
            else:
                messages.error(request, "Invalid Password ❌")
        else:
            messages.error(request, "Doctor not found ❌")
            return render(request, 'sigin_page.html')

    return render(request,'sigin_page.html')

 #otp page
def verify_otp(request):

    if request.method == "POST":

        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if str(user_otp) == str(session_otp):

           
            

           
            messages.success(request, "OTP Verified Successfully ✅")

            return redirect(doctor_page)

        else:
            messages.error(request, "Invalid OTP ❌")

            return render(request,'otp_page.html',{'error':'Invalid OTP'})

    return render(request,'otp_page.html')

# Doctor Page View
def doctor_page(request):
    username = request.session.get('username')
    doctor = doctordb.objects.filter(doc_name=username).first()

    return render(request, "doctor_page.html", {"username": username, "doctor": doctor})

#doctor page logout
def doctor_logout(request):
    username = request.session.get('username')

    if not username:
       return redirect(sigin_page)
    del request.session['username']
    del request.session['password']
    
    return redirect(sigin_page)

       
    
    
    