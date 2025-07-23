from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'), # localhost:8000
    path('about/', about_page, name='about'),
    path('contact/', contact, name='contact'),
    path('course/<int:id>/', course, name='course'),
    path('profile/', student_profile, name='student_profile'),
    path('login/', login_page, name='login'),
    path('courses/<str:course_title>/', course, name='course'),
]