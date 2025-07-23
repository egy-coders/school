from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *

# Create your views (controller) here.
"""
Students - courses - exams
"""
# login() function built in django - operation login (authetication)
# login page to display the html login page
def login_page(request):
    return render(request, 'login.html')

def home_page(request):
    # return HttpResponse('Home Page')
    # courses = Course.objects.filter(featured=True)[:1] # limit items
    courses = Course.objects.all()
    context = {
        'page_title' : 'Home Page',
        'courses':courses
    }
    return render(request, 'home.html', context)


def about_page(request):
    context = {
        'page_title' : 'About Us'
    }
    return render(request, 'about.html' , context)

def contact(request):
    context = {
        'page_title' : 'Contact'
    }
    return render(request, 'contact.html' , context)

def course(request, course_id):
    context ={
        'id':1,
        'title':'python',
        'price':'220'
    }
    return render(request, 'course.html',context)


def student_profile(request):
    return render(request, 'students/profile.html')


def course(request, course_title):
    course = Course.objects.get(title=course_title) # more than one record - error
    context = {
        'course':course,
        'page_title' : course.title
    }

    return render(request, 'course.html', context)