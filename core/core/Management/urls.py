from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('managementlogin/',views.managementlogin,name="managementlogin"),
    path('patientlogin/',views.patientlogin,name="patientlogin"),
    path('createpatient/',views.createpatient,name="createpatient"),
    path('createreport/',views.createreport,name="createreport"),
    path('checkmobile/',views.checkmobile,name="checkmobile"),
    path("Management-control",views.management,name="management-control"),
    path("allreports/",views.allreports,name="allreports"),
    path("createmanager/",views.createManager,name="createmanager"),
    path("logoutuser/",views.logoutuser,name="logoutuser"),
    path("userreports",views.userreports,name="userreports")
]