from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Username'
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))
    class Meta:
        model = CustomUser
        # fields = ['username','password']
        fields = ('__all__')

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Input Username'
            }
    ))
    email = forms.CharField(label='Email', widget=forms.TextInput(
            attrs={
               'class' : 'form-control',
                'placeholder' : 'Input Email'
            }
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Password'
        }
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        }
    ))
    user_type = forms.ChoiceField(choices = [
        ('','-Select an option-'),
        ('job_seeker','Job Seeker'),
        ('recruiter','Recruiter'),
    ],widget = forms.Select(attrs={
        "class":"form-select w-50"
    }))
    # user_type = forms.CharField(label='User Type', widget=forms.TextInput(
    #     attrs={
    #         'class' : 'form-control',
    #         'placeholder' : 'User Type'
    #     }
    # ))
    display_name = forms.CharField(label='Display Name', widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Display Name'
        }
    ))

    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2','user_type','display_name']
        # fields = ('__all__')
class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = Job_seeker
        fields = ('__all__')

class JobRecruiterForm(forms.ModelForm):
    class Meta:
        model = Job_recruiter
        fields = ('__all__')

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('__all__')