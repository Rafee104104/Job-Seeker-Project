from django.shortcuts import render, redirect
from django.http import request
from .models import *
from django.contrib.auth import *
import random
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    jobs = Job.objects.all()
    
    context = {
        "jobs": jobs
    }
    return render(request, 'homepage.html', context)


def registration(request):
    if(request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            # user.set_password(form.cleaned_data.get('password1')])
            user.save()
            return redirect('userlogin')
    else:
        form = RegistrationForm()
    return render(request,'registrationform.html',{'form':form})


def userlogin(request):
    if request.method=="POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
    else:
        form = LoginForm()

    return render(request,'loginForm.html',{'form':form})

def update_pass(request):
    if request.method== "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_pass = request.POST.get('new_pass')
        confirm_pass = request.POST.get('confirm_pass')
        user = CustomUser.objects.get(email=email)
        if user.otp != int(otp):
            context = {
                'error' : 'Your OTP is invalid'
            }
            return render(request, 'update_pass.html',context)
        if new_pass != confirm_pass:
            context ={
                'error' : 'Your password do not mactched'
            }
            return render(request,'update_pass.html',context)
        user.set_password(new_pass)
        user.otp = None
        user.save()
        return redirect('userlogin')
    return render(request,'update_pass.html')

def send_otp(request):
    
    if request.method == "POST":
        email = request.POST.get('email')

        user =CustomUser.objects.get(email=email)

        otp = random.randint(111111,999999)
        user.otp =otp
        user.save()

        email_sub=f"""Your Forget Password OTP {otp}"""
        msg=f"""Your Forget Password OTP is {otp} \nPlease Don't Share Your OTP with Anyone."""
        from_email= EMAIL_HOST_USER
        to_email=email

        send_mail(
            subject=email_sub,
            message=msg,
            from_email=from_email,
            recipient_list=[to_email]
        )

        return redirect('update_pass')
    return render(request, 'forget_pass.html')

@login_required
def addJobForm(request):
    if request.method == "POST":
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = JobForm()
    return render(request,'addJobForm.html',{'form':form})

@login_required
def editJobForm(request,my_id):
    if request.method == "POST":
            form = JobForm(request.POST,instance=Job)
            if form.is_valid():
                form.save()
                return redirect('homepage')
    else:
        form = JobForm()
    return render(request,'editJobForm.html',{'form':form})
@login_required
def deleteJobForm(request,my_id):
    job = Job.objects.get(id=my_id)
    job.delete()
    return redirect('homepage')

@login_required
def set_profile(request):
    if request.method == "POST":
        form = JobRecruiterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('set_profile')
    else:
        form = JobRecruiterForm()
    return render(request,'set_profile.html',{'form':form})
@login_required
def user_logout(request):
    logout(request)
    return redirect('registration')