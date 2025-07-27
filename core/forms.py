from django import forms
from .models import Course



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
            'publish_on': forms.TextInput(attrs={
                'class':'form-control',
                'type':'datetime-local'
            })
        }
