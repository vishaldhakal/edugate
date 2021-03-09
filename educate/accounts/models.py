from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Student(models.Model):
    avatar = models.FileField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    no_of_courses_enrolled = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    avatar = models.FileField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    brief_introduction = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    no_of_published_course = models.IntegerField(default=0)
    no_of_enrolled_students = models.IntegerField(default=0)
    average_review_ratings = models.IntegerField(default=0)
    num_of_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username