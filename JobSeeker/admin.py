from django.contrib import admin
from .models import CustomUser,Job,JobSeekerProfile,JobRecruiterProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Job)
admin.site.register(JobRecruiterProfile)
admin.site.register(JobSeekerProfile)