from django.db import models

"""
Network one (category) - many (courses)  (CCNA - MSCE - Networking)
Web Development (Django - Flask - ...) # CASCADE - SET_NULL

Django one - to - one (Web Develop ) NULL
CCNA (Network)

One - to -  one

student -> profile (1)
profile related to (1) student

"""

# ORM
"""
Object-relation mapper
sql
select * from studets where is_active=true

Native sql
Select all courses under some category
select cat.name, course.title from courses left join courses on cat.id = course.cat_id

ORM
Model.object.all() retrieve all data
Model.objetcs.first() first record
Model.objetcs.latest() last record

Model.objetcs.get(id=x) # Get one item 
Model.objects.filter(name=xxx) # filter list of items []

Backward - reverse relationships 

ParentModel.childmodel_set.all() # reserved keyword _set | related_name = ''
cat1 = Cat.objetcs.get(id=1)
cat1.course_set.all()  # default related_name
cat1.courses.all()  # related_name = courses

one to one
Model.model
Student.profile -> profile related to this student
Profile.student -> Student related to this profile


many to many
students - courses
C++ (Mohamed - Ahmed - ...)
Mohamed (C++, python, Java, ....)

course1 = Course.objetcs.get(id=1)
course1.student_set.all() # default related_name
course1.students.all() # related_name = students

"""

class Cat(models.Model): # Parent Super One side
    # id = model.Integer(autp)
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"

class Course(models.Model): # Many Side - child
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
    )
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name="courses", null=True) # cat_id
    title = models.CharField(max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES)
    # students = 

    def __str__(self):
        return f"{self.title}"
    
class Student(models.Model):
    GRADE_CHOICES = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),

    )
    name = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)
    grade = models.CharField(choices=GRADE_CHOICES)
    courses = models.ManyToManyField(Course, related_name='students')

    

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    image = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.student} | {self.phone}"

