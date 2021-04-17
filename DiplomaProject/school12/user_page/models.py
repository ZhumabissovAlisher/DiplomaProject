from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'img/%y')

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    subject_teacher = models.CharField(max_length = 100)
    facebook = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'img/%y')
    
    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_title = models.CharField(max_length = 100)
    course_description = models.TextField()
    course_image = models.ImageField(upload_to = 'img/%y')

    def __str__(self):
        return self.course_title

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'img/%y')

    def __str__(self):
        return self.title



