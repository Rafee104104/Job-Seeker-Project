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
    """
    (Title, Number of openings, Category, 
Job description, Skills set)
    """

    def __str__(self):
        return self.username


class JobRecruiterProfile(models.Model):

    users = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact_number = models.IntegerField(max_length=30)
    contact_email = models.EmailField(max_length=40)
    company_logo = models.ImageField(upload_to='media/company_logo/',blank=True,null=True)

    def __str__(self):
        return self.users.username

class JobSeekerProfile(models.Model):
    
    users = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone_number = models.IntegerField(max_length=30)
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/JobSeekerImage/',blank=True,null=True)
    cv = models.FileField(upload_to='media/JobSeekerCV/',blank=True,null=True)

## skills = models.TextField(null = True, blank = True)

    def __str__(self):
            return self.users.username
    
class Job(models.Model):
    JOB_TYPES = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
        ("remote", "Remote"),
    ]

    EXPERIENCE_LEVELS = [
        ("entry", "Entry Level"),
        ("mid", "Mid Level"),
        ("senior", "Senior Level"),
    ]

    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    requirements = models.CharField(max_length=100)

    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    experience_level = models.CharField(max_length=20,choices=EXPERIENCE_LEVELS)

    salary_range = models.CharField(null=True,blank=True)

    vacancies = models.IntegerField(null=True,blank=True)
    application_deadline = models.CharField()
    is_active = models.BooleanField(default=True)
    is_applied = models.BooleanField(default=False) # Remove this 
    Published=models.CharField(max_length=100)
    age_range = models.CharField(max_length=20)

    def __str__(self):
        return self.title