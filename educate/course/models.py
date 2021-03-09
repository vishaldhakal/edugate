from django.db import models
from accounts.models import Student,Teacher

class Course(models.Model):
    thumbnail = models.FileField(blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="tec")
    students = models.ManyToManyField(Student,blank=True)
    course_name = models.CharField(max_length=400)
    release_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    course_description = models.TextField(blank=True)

    def __str__(self):
        return self.course_name


class WhatWillYouLearn(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    what_to_learn = models.TextField()

    def __str__(self):
        return self.what_to_learn


class WhatToKnow(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    what_to_know = models.TextField()

    def __str__(self):
        return self.what_to_know

class Topic(models.Model):
    name = models.CharField(max_length=400)
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ContentType(models.Model):
    CONTENT_CHOICES = [
        ("video", "video"), 
        ("other", "other"),
    ]  
    content_type = models.CharField(max_length=500,choices=CONTENT_CHOICES)



class Lesson(models.Model):
    name = models.CharField(max_length=400)
    topi = models.ForeignKey(Topic,blank=True,on_delete=models.CASCADE)
    video = models.FileField()
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

 