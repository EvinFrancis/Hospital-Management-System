from django.urls import path
from . import views

urlpatterns = [

    path('', views.user_profile, name='user_profile'),
    path('appointment_page/', views.appointment_page, name='appointment_page'),
    path('get-doctors/', views.get_doctors, name="get_doctors"),
    path('booking_appointment/', views.booking_appointment, name="booking_appointment"),
    path('payment_success/', views.payment_success, name="payment_success"),
    path('ai_chatbot/', views.ai_chatbot, name="ai_chatbot"),


]