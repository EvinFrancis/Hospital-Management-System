from django.urls import path
from adminapp import views
urlpatterns = [
    
    path("admin_page/",views.admin_page,name="admin_page"),
    path("",views.admin_loginpage,name="admin_loginpage"),
    path("admin_login",views.admin_login,name="admin_login"),
]
