from django.urls import path, include
from . import views
urlpatterns = [
    path('course/<name>/',views.single,name="single"),
    path('course/addreview/<name>/',views.add_review,name="add_review"),
    path('',views.index,name="index"),
    path('teacher/',views.teacherindex,name="teacherindex"),
    path('teacher/courses/',views.teachercourses,name="teachercourses"),
    path('teacher/course/<name>/',views.course_dashboard,name="course_dashboard"),
    path('teacher/course/delete/topic/<name>/',views.delete_topic,name="delete_topic"),
    path('teacher/course/update/topic/<name>/',views.update_topic,name="update_topic"),
    path('teacher/course/delete/lesson/<name>/',views.delete_lesson,name="delete_lesson"),
    path('teacher/course/update/lesson/<name>/',views.update_lesson,name="update_lesson"),
    path('enroll/<int:id>/',views.enrollment,name="enrollment"),
    path('course/enrolled/<name>/',views.after_enrollment_course,name="after_enroll"),
    path('courses_list/',views.course_list,name="course_list"),
    path('add/course/',views.add_course,name="addcourse"),
    path('add/topic/',views.add_topic,name="addtopic"),
    path('add/lesson/',views.add_lesson,name="addlesson"),
    path('add/whattoknow/',views.add_whattoknow,name="whattoknow"),
    path('add/whatwillyoulearn/',views.add_whatwillyoulearn,name="whatwillyoulearn"),
]