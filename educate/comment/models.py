from django.db import models
from accounts.models import Student,Teacher
from course.models import Course as cour
from ratings.models import Rate as rt

class Comment(models.Model):
    fromm = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(cour,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.fromm.user.username

    def get_replies(self):
        return Reply.objects.filter(comment=self)

    def get_rating(self):
        return rt.objects.get(student=self.fromm)


class Reply(models.Model):
    fromm = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(cour,on_delete=models.CASCADE)
    content = models.TextField()
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)

    def __str__(self):
        return self.fromm.user.username