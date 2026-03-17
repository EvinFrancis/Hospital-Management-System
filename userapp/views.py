from django.shortcuts import render,redirect
from adminapp.models import *
from userapp.models import *
from twilio.rest import Client
import os 
from dotenv import load_dotenv
load_dotenv()
# Create your views here.


# howm page user profile

def user_profile(request):
    return render(request,'home_page.html')

def appointment_page(request):
    departments=departmentdb.objects.all()
    
    
    return render(request,'Appointment.html',{'departments':departments})


# ajax docotr view
#AJAX Doctor View

from django.http import JsonResponse
from adminapp.models import doctordb

def get_doctors(request):

    department = request.GET.get('department')

    doctors = doctordb.objects.filter(doc_dpt=department)

    data = []

    for doctor in doctors:
        data.append({
            "id": doctor.id,
            "name": doctor.doc_name
        })

    return JsonResponse(data, safe=False)

# apooinment booking
from django.contrib import messages

def booking_appointment(request):
    if request.method == "POST":

        obj = appointmentdb()

        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.department = request.POST.get('department')
        obj.doctor = request.POST.get('doctor')
        obj.date = request.POST.get('date')
        obj.message = request.POST.get('message')

        

        # ✅ Call SMS function
        result = send_sms(obj.phone, obj.name, obj.date)

        # ✅ Handle responses
        if result == "unverified":
            messages.error(request, "Phone number is not verified in Twilio.")
        elif result == "from_error":
            messages.error(request, "Twilio number configuration error.")
        elif result == "other_error":
            messages.error(request, "SMS failed. Try again later.")
        else:
            obj.save()
            messages.success(request, "Appointment booked & SMS sent!")

    return redirect(appointment_page)



#twilo send messages

from twilio.base.exceptions import TwilioRestException


def send_sms(phone, name, date):
    
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=f"Hi {name}, your appointment is booked on {date}. See you soon!",
            from_='+17855466511',
            to=f"+91{phone}"
        )
        return "success"

    except TwilioRestException as e:
        print("Twilio Error:", e.code, e.msg)

        if e.code == 21608:
            return "unverified"

        elif e.code == 21660:
            return "from_error"

        else:
            return "other_error"

