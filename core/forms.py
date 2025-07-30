from django import forms
from django.core.exceptions import ValidationError
from .models import Course, Student
from django.utils import timezone



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        labels = {
            'cat' : 'Course Category',
            'title' : 'Course Title'
        }

        widgets = {
            'cat': forms.Select(attrs={
                'class':'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Course Title'
            }),
            'level': forms.Select(attrs={
                'class':'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'max':'999.99',
                'step':'0.01'
            }),
            'description': forms.Textarea(attrs={
                'class':'form-control',
                'rows':2
            }),
            'publish_on': forms.TextInput(attrs={
                'class':'form-control',
                'type':'datetime-local'
            })
        }

    # Validation Rules | cleaned_data 
    def clean_cat(self):
        cat = self.cleaned_data.get('cat')
        if not cat:
            raise ValidationError("Category is required")
        return cat
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not 5 <= len(title) <= 50: 
            raise ValidationError("Course Title must be between 5 and 50 chars")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not 5 <= len(description) <= 50: 
            raise ValidationError("Course Description must be between 5 and 50 chars")
        return description
    
    def clean_publish_on(self):
        publish_on = self.cleaned_data.get('publish_on')
        if publish_on and publish_on < timezone.now():
            raise ValidationError("Publish date must be in future")
        return publish_on
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0 :
            raise ValidationError("Price must be greater than or equal 0")
        return price
    
    def clean(self):
        cleaned_data = super().clean()
        level = cleaned_data.get('level') # Advanced
        featured = cleaned_data.get('featured')  # True

        if level == 'advanced' and not featured:
            self.add_error('featured', 'Advanced Courses mus be marked as featured!')

import re

class StudentForm(forms.ModelForm):
    # email validator
    def validate_email(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None
    
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'name' :'Full Name',
            'dob' : 'Date of birth',
        }

        widgets = {
            'name' : forms.TextInput(attrs={
                'class':'form-control',
                'required':True,
                'placeholder':'Enter Full Name'
            }),
            'email' : forms.TextInput(attrs={
                'class':'form-control',
                'required':True,
            }),
            'dob' : forms.TextInput(attrs={
                'class':'form-control',
                'required':True,
                'type':'date'
            }),
            'grade' : forms.Select(attrs={
                'class':'form-control',
                'required':True,
            }),
            'courses' : forms.SelectMultiple(attrs={
                'class':'form-control',
                'required':True,
            }),
            
        }