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


class Job_seeker(models.Model):
    username=models.CharField(max_length=30),
    first_name=models.CharField(max_length=30),
    last_name=models.CharField(max_length=30),
    email=models.EmailField(max_length=30),
    date_of_birth=models.CharField(max_length=30),
    religion=models.CharField(max_length=30),
    gender=models.CharField(max_length=30),
    marital_status=models.CharField(max_length=30),
    nationality=models.CharField(max_length=30),
    mobile_phone_number=models.CharField(max_length=30),
    blood_group=models.CharField(max_length=30),
    image=models.ImageField(upload_to='job_seeker/profile/',blank=True,null=True),
    cv=models.FileField(upload_to='job_seeker/CV/',blank=True,null=True)
    def __str__(self):
        return self.username

class Job_recruiter(models.Model):
    username=models.CharField(max_length=30),
    first_name=models.CharField(max_length=30),
    last_name=models.CharField(max_length=30),
    email=models.EmailField(max_length=30),
    date_of_birth=models.CharField(max_length=30),
    religion=models.CharField(max_length=30),
    gender=models.CharField(max_length=30),
    marital_status=models.CharField(max_length=30),
    nationality=models.CharField(max_length=30),
    mobile_phone_number=models.CharField(max_length=30),
    blood_group=models.CharField(max_length=30),
    image=models.ImageField(upload_to='job_seeker/profile/',blank=True,null=True)
    def __str__(self):
        return self.username


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

    salary_min = models.IntegerField(null=True,blank=True)
    salary_max = models.IntegerField(null=True,blank=True)

    vacancies = models.IntegerField(null=True,blank=True)
    application_deadline = models.CharField()
    is_active = models.BooleanField(default=True)
    is_applied = models.BooleanField(default=False)
    Published=models.CharField(max_length=100)
    deadline = models.CharField(max_length=20)
    age_range = models.CharField(max_length=20)

    def __str__(self):
        return self.title