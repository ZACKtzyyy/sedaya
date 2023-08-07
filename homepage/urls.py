from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.loginpage, name="loginpage"),
    path("feedback/", views.feedback, name="feedback"),
    path("addevents/", views.addevents, name="addevents"),
    path("membership/", views.MembershipRegister.as_view(), name="membership"),
    path("loginpage/", views.loginpage, name="loginpage"),
    path("register/", views.register, name="register"),
    path("register/success/", views.register_success, name="register_success"),
    path("adminhomepage/", views.adminhomepage, name="adminhomepage"),
    path("achievement/", views.achievement, name="achievement"),
    path("viewevents/", views.viewevents, name="viewevents"), 
    path("viewachievements/", views.viewachievements, name="viewachievements"),
    path('about/', views.about, name='about'),
    path("adminloginpage/", views.adminloginpage, name="adminloginpage"),
    path("manageevents/", views.manageevents, name="manageevents"),
    path('deleteevent/<str:eventName>/', views.deleteevent, name='deleteevent'),
    path('updateevent/<str:eventName>/', views.updateevent, name='updateevent'),
    path('addachievement/', views.addachievement, name='addachievement'),
    path('viewach/', views.viewach, name='viewach'),
    path('membershiplogin/', views.membershiplogin, name='membershiplogin'),
    path('managemember/', views.managemember, name='managemember'),
    path('delete_member/<str:memberid>/', views.delete_member, name='delete_member'),
    path('updatemember/<str:memberid>/', views.updatemember, name='updatemember'),
    path('membershiplogin/', views.membershiplogin, name='membershiplogin'),
    path("userhomepage/", views.userhomepage, name="userhomepage"),

]









