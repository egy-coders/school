from django.db import models

"""
Students:
- name
- age
- enrolled_at

Create Database School
Use School
create table student (
name (string, unique)
age
.
.
)

ORM (Object Relation Mapper) 
select
update
delete

Code First - pattern
"""
# students table
class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    enrolled_at = models.DateField()

# Web Development - Data Science - Networking
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"

# courses table
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cateory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cateory} - {self.title}"