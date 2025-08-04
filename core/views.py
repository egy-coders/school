from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views (controller) here.
"""
Students - courses - exams
CRUD 
Create Read Update Delete (generic views) - view sets API 
"""
# login() function built in django - operation login (authetication)
# login page to display the html login page
def login_page(request):
    return render(request, 'login.html')

def home_page(request):
    # return HttpResponse('Home Page')
    # courses = Course.objects.filter(featured=True)[:1] # limit items
    courses = Course.objects.order_by('-id')
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

    if request.method == 'POST':
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        message = request.POST.get('message')
        data = [name, email, phone,message]
        return HttpResponse(data)

   
    context = {
        'page_title' : 'Contact'
    }
    return render(request, 'contact.html' , context)

def student_profile(request):
    return render(request, 'students/profile.html')

# Display Single Course
def course(request, course_id): # id (int) = pk (str) 1 = '1'
    course = get_object_or_404(Course, id=course_id)
    context = {
        'course':course,
        'page_title' : course.title
    }

    return render(request, 'course.html', context)

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid(): # not only validation rules - form not crashed
            form.save()
            messages.success(request, 'Course Saved Successfully')
            return redirect('home')
        else:
            messages.error(request, "Failed to saved course")
    else:
        form = CourseForm()

    context  = {
        'page_title':'Create Course',
        'form': form
    }
    return render(request, 'course_form.html', context)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Saved Successfully') # success
            return redirect('home')
        else:
            messages.error(request, 'Failed to save student') # error
    else:
        form = StudentForm()

    context = {
        'page_title':'Create Student',
        'form':form
    }
    return render(request, 'create_student.html', context)

def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id) # course object
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated!')
            return redirect('course', course.id)
        else:
            messages.error(request, 'Failed to update')
    else:
        form = CourseForm(instance=course)
    
    context = {
        'page_title':f'Update Course {course.title}',

        'form': form,
        'course':course,
    }

    return render(request, 'course_form.html', context)

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id) # retreive from database
    previous_url = request.META.get("HTTP_REFERER", reverse('home'))
    if request.method == 'POST':
        course.delete()
        messages.success(request, f"{course.title} deleted successfully!")
        return redirect("home")
    
    context = {
        'course':course,
        'page_title':f'Delete {course.title}',
        'previous_url' : previous_url
    }

    return render(request, 'confirm_delete.html', context)