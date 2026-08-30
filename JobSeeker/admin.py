from django.contrib import admin
from .models import CustomUser,Job,Job_recruiter,Job_seeker
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Job)
admin.site.register(Job_recruiter)
admin.site.register(Job_seeker)