from django.db import models
from accounts.models import Student
from course.models import Course as cour

class Rating(models.Model):
    course = models.ForeignKey(cour,on_delete=models.CASCADE)
    rating_value = models.IntegerField(default=0)
    total_no_of_ratings = models.IntegerField(default=0)

class Rate(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(cour,on_delete=models.CASCADE)
    rating = models.IntegerField()

    def ratee(self):
        return self.rating * 10
