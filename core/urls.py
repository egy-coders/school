from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'), # localhost:8000
    path('about/', about_page, name='about'),
    path('contact/', contact, name='contact'),
    path('course/<int:course_id>/', course, name='course'),
    path('profile/', student_profile, name='student_profile'),
    path('login/', login_page, name='login'),


    path('create-course/', create_course, name='create_course'),
    path('update-course/<int:course_id>/', update_course, name='update_course'),
    path('delete-course/<int:course_id>/', delete_course, name='delete_course'),
    path('create-student/', create_student, name='create_student'),
]