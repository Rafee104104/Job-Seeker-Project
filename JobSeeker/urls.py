from django.urls import path
from .views import *

urlpatterns = [
    path('',registration,name='registration'),    
    path('userlogin/',userlogin,name='userlogin'),
    path('editJobForm/<int:my_id>',editJobForm,name='editJobForm'),
    path('addJobForm/',addJobForm,name='addJobForm'),
    path('deleteJobForm/<int:my_id>',deleteJobForm,name='deleteJobForm'),
    path('homepage/',homepage,name='homepage'),
    path('set_profile/',set_profile,name='set_profile'),
    path('user_logout/',user_logout,name='user_logout'),
    path('update_pass/',update_pass,name='update_pass'),
    path('forget_pass/',send_otp,name='forget_pass')   
]