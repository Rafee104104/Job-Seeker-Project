from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = {
        ('jobSeeker','JobSeeker'),
        ('jobRecruiter','JobRecruiter')
    }
    display_name = models.CharField(max_length=255)
    otp = models.IntegerField(blank=True,null=True)    
    user_type = models.CharField(max_length=50,choices= USER,null=True)
    

    def __str__(self):
        return self.username


class JobRecruiterProfile(models.Model):

    users = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING, related_name= 'jobrecruiterprofile')
    company_name = models.CharField(max_length=30 , null= True, blank= True)
    location = models.CharField(max_length=30 , null= True, blank= True)
    contact_number = models.IntegerField(null= True, blank= True)
    contact_email = models.EmailField(max_length=40 , null= True, blank= True)
    company_logo = models.ImageField(upload_to='media/company_logo/',blank=True,null=True)

    def __str__(self):
        return self.users.username

class JobSeekerProfile(models.Model):
    
    users = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING, related_name= 'jobseekerprofile')
    name = models.CharField(max_length=30 , null= True, blank= True)
    email = models.EmailField(max_length=40 , null= True, blank= True)
    phone_number = models.IntegerField( null= True, blank= True)
    location = models.CharField(max_length=30 , null= True, blank= True)
    image = models.ImageField(upload_to='media/JobSeekerImage/',blank=True,null=True)
    cv = models.FileField(upload_to='media/JobSeekerCV/',blank=True,null=True)

## skills = models.TextField(null = True, blank = True) 

    def __str__(self):
            return self.users.username
    
class Job(models.Model):

    title = models.CharField(max_length=200 , null= True, blank= True)
    number_of_opening = models.IntegerField( null= True, blank= True)
    category = models.TextField(max_length=100 , null= True, blank= True)
    description = models.TextField(max_length=1000 , null= True, blank= True)
    skills_set = models.TextField(max_length=700 , null= True, blank= True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title