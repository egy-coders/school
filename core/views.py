from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views (controller) here.
"""
Students - courses - exams
"""

def home_page(request):
    # return HttpResponse('Home Page')
    courses = [
        {
            'id':1,
            'title':'python',
            'price':220
        },
        {
            'id':2,
            'title':'C#',
            'price':250
        },
        {
            'id':3,
            'title':'C++',
            'price':300
        },
    ] 
    # Model Courses 
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
