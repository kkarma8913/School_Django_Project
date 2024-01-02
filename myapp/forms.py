
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator  

class CustomerRegistrationForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
 email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
 class Meta:
  model = User
  fields = ['username', 'email', 'password1', 'password2']
  labels = {'email': 'Email'}
  widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
 username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
 password = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class':'form-control'}))



class admissionform(forms.ModelForm):
    student_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    admission_for=models.CharField(max_length=10,choices=admission_choices)
    father_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])  
    father_Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])  
    mother_name=models.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])  
    mother_Contact_no=models.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])
  

    class Meta:
       
        model=admission
        fields ='__all__'
        widgets ={'date_of_birth':forms.DateInput(attrs={'type':'date'})}

class feedbackform(forms.ModelForm):
    full_name=forms.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    Contact_no=forms.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")])
    
 
    class Meta:
       
        model=feedback
        fields ='__all__'
        

class contactform(forms.ModelForm):
    First_name=forms.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])
    last_name=forms.CharField(max_length=20,validators=[RegexValidator("[a-zA-Z][a-zA-Z ]+[a-zA-Z]$",message="Enter only Alphabets")])

    Contact_no=forms.CharField(max_length=10,validators=[RegexValidator("^[0-9]*$",message="Enter only Numbers")]) 
 
    class Meta:
       
       model=contact_us
       fields ='__all__'
