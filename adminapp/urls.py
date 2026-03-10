from django.urls import path
from adminapp import views
urlpatterns = [
    
    path("admin_page/",views.admin_page,name="admin_page"),
    path("",views.admin_loginpage,name="admin_loginpage"),
    path("admin_login",views.admin_login,name="admin_login"),
    path("admin_logout",views.admin_logout,name="admin_logout"),
    path("view_doctors",views.view_doctors,name="view_doctors"),
    path("view_departments",views.view_departments,name="view_departments"),
    path("save_department",views.save_department,name="save_department"),
]
