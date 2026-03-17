from django.urls import path
from doctorsapp import views

urlpatterns = [
    
    path('sigin_page/',views.sigin_page,name="sigin_page"),
    path('doctor_login/',views.doctor_login,name="doctor_login"),
    path('doctor_page/',views.doctor_page,name="doctor_page"),
    path('doctor_logout/',views.doctor_logout,name="doctor_logout"),
    path('verify_otp/',views.verify_otp,name='otp_page'),

   
]