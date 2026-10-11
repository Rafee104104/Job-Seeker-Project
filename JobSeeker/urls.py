from django.urls import path
from .views import *

urlpatterns = [
    path('',registration,name='registration'),    
    path('userlogin/',userlogin,name='userlogin'),
    path('editJobForm/<int:my_id>',editJobForm,name='editJobForm'),
    path('addJobForm/',addJobForm,name='addJobForm'),
    path('deleteJobForm/<int:my_id>',deleteJobForm,name='deleteJobForm'),
    path('homepage/',homepage,name='homepage'),
    path('searchTitle/',searchTitle,name='searchTitle'),
    path('user_logout/',user_logout,name='user_logout'),
    path('update_pass/',update_pass,name='update_pass'),
    path('forget_pass/',send_otp,name='forget_pass'),
    path('jobRecruiterProfile/',jobRecruiterProfile,name='jobRecruiterProfile'),
    path('jobSeekerProfile/',jobSeekerProfile,name='jobSeekerProfile'),
    path('updateJobRecruiterProfile/',updateJobRecruiterProfile,name='updateJobRecruiterProfile'),
    path('updateJobSeekerProfile/',updateJobSeekerProfile,name='updateJobSeekerProfile'),
    path('search_skills_set/',search_skills_set,name='search_skills_set'),
    path('viewJob/<int:id>',viewJob,name='viewJob')    
]