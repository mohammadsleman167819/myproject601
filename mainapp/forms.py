from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","role")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email","role")

from django import forms
from datetime import date


class EmployeeInfoForm(forms.Form):
    firstname = forms.CharField(label="First Name", max_length=100, help_text='Employee First Name')
    lastname = forms.CharField(label="Last Name", max_length=100, help_text='Employee Last Name')
    dateOfBirth = forms.DateField(label="Date Of Birth", help_text='Employee Date of Birth')
    gender = forms.ChoiceField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], label="Gender")
    city = forms.CharField(label="City", max_length=50, help_text='Employee City')
    phone = forms.CharField(label="Phone", max_length=20,min_length=10, help_text='Employee Phone')
    education = forms.CharField(widget=forms.Textarea,label="Education", max_length=1000, required=False)  
    experience = forms.CharField(widget=forms.Textarea,label="Experience", max_length=1000, required=False)  
    awards = forms.CharField(widget=forms.Textarea,label="Awards", max_length=1000, required=False)  
    hobbies = forms.CharField(widget=forms.Textarea,label="Hobbies", max_length=1000, required=False)  
    skills = forms.CharField(widget=forms.Textarea,label="Skills", max_length=1000)
    references = forms.CharField(widget=forms.Textarea,label="References", max_length=1000, required=False)  
    other = forms.CharField(widget=forms.Textarea,label="Other", max_length=1000, required=False)  
    def clean_phone(self):
        data = self.cleaned_data['phone']

        for char in data:
           if not char.isdigit() and char not in '-+':
                raise ValidationError('Phone number can only contain digits, hyphens, and plus signs.')

        return data

    def clean_date_of_birth(self):       
        data = self.cleaned_data['date_of_birth']
        today = date.today()
        if data > today:
            raise ValidationError('Date of birth cannot be in the future.')
        minimum_age = 16 
        maximum_age = 120  
        
        age = today.year - data.year - ((today.month, today.day) < (data.month,data.day))
        if age < minimum_age:
            raise ValidationError(f'You must be at least {minimum_age} years old to register.')
        if age > maximum_age:
            raise ValidationError(f'{age} years old is not a valid value.')

        return data


class CompanyInfoForm(forms.Form):
    name  = forms.CharField(label="Comapany Name",max_length=100) 
    city = forms.CharField(label="City", max_length=50)
    phone = forms.CharField(label="Phone", max_length=20,min_length=10)
    

    def clean_phone(self):
        data = self.cleaned_data['phone']

        for char in data:
           if not char.isdigit() and char not in '-+':
                raise ValidationError('Phone number can only contain digits, hyphens, and plus signs.')

        return data

    
class Job_PostCreateForm(forms.Form):
    
    job_title = forms.CharField(label="Job Title",max_length=50) 
    jobDescription = forms.CharField(widget=forms.Textarea,label="Job Description", max_length=1000)
    workhours = forms.CharField(widget=forms.Textarea,label="Work Hours", max_length=1000)
    contact = forms.CharField(label="Contact",max_length=50)
    city = forms.CharField(label="City", max_length=50)
    salary = forms.CharField(label="Salary", max_length=50)
    

class CourseCreateForm(forms.Form):
    
    courseTitle = forms.CharField(label="Course Title",max_length=50)
    description  = forms.CharField(widget=forms.Textarea,label="Course Description", max_length=1000)
    link = forms.CharField(label="Course Link", max_length=100)
    

