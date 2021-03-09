from django.shortcuts import render, redirect, HttpResponse
from .models import Course,Topic,Lesson,WhatWillYouLearn,WhatToKnow, ContentType
from accounts.models import Student as std, Teacher as tch,User as use
from comment.models import Comment as cmt,Reply as rep
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from ratings.models import Rate as rate
import os

def single(request,name):
    course = Course.objects.get(course_name=name)
    topics = Topic.objects.filter(course=course)
    what_to_learn = WhatWillYouLearn.objects.filter(course=course)
    what_to_know = WhatToKnow.objects.filter(course=course)
    comments = cmt.objects.filter(course=course)
    students_in_course = course.students.all()
    check = 0
    for student in students_in_course:
        if (student.user.id == request.user.id):
            check = 1
            break
        else:
            check = 0
    lessons = []
    context = {'course':course,'topics':topics,'whatyoulearn':what_to_learn,'whattoknow':what_to_know,'comments':comments,'check':check}
    for key,topic in enumerate(topics):
        lesson = Lesson.objects.filter(topi=topic)
        lessons.append(lesson)
    context.update({'lessons' : lessons})

    return render(request, 'course.html',context)

def index(request):
    courses_top_4 = Course.objects.all().order_by('release_date')[:4]
    context = {
        'courses':courses_top_4
    }
    if request.user.is_superuser:
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html',context)




def teacherindex(request):
    teacher = tch.objects.get(user = request.user)
    courses = Course.objects.filter(teacher = teacher)
    topics = Topic.objects.all()
    context = {
        'courses':courses,
        'topics':topics
    }
    return render(request, 'teacherdash.html',context)

def teachercourses(request):
    user = request.user
    teacher = tch.objects.get(user=user)
    courses = Course.objects.filter(teacher=teacher)
    context = {
        'courses':courses
    }
    return render(request,'teacher_courses.html',context)

def add_review(request,name):
    course = Course.objects.get(course_name=name)
    student = std.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST["comment"]
        rating = request.POST["rating"]
        rat = rate(student=student,course=course,rating=rating)
        comment = cmt(fromm=student,course=course,content=comment)
        comment.save()
        rat.save()

    return redirect('single',name=name)

def add_course(request):
    user = request.user
    teacher = tch.objects.get(user=user)
    if request.method == "POST":
        name = request.POST['course_name']
        description = request.POST['course_description']
        thumbnail = request.FILES["thumbnail"]
        fs = FileSystemStorage()
        filename = fs.save(thumbnail.name, thumbnail)
        course = Course(thumbnail=filename,teacher=teacher,course_name=name,course_description=description)
        course.save()
    
    return redirect('teacherindex')

def add_topic(request):
    user = request.user
    teacher = tch.objects.get(user=user)
    if request.method == "POST":
        course_name = request.POST['course_select']
        topic_name = request.POST['topic_name']
        course = Course.objects.get(course_name=course_name)
        topic = Topic(name=topic_name,course=course)
        topic.save()
    
    return redirect('teacherindex')

def add_lesson(request):
    user = request.user
    teacher = tch.objects.get(user=user)
    if request.method == 'POST' and request.FILES['myfile']:
        topic = request.POST['topic_select']
        lesson_name = request.POST['lesson_name']
        myfile = request.FILES['myfile']
        content = request.POST['type_select']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        topic = Topic.objects.get(name=topic)
        cont = ContentType(content_type=content)
        cont.save()
        lesson = Lesson(name=lesson_name,topi=topic,video=filename,content_type=cont)
        lesson.save()
    
    return redirect('teacherindex')

def add_whattoknow(request):
    if request.method == "POST":
        course = request.POST['course_select']
        what_to_know = request.POST['what_to_learn']
        cours = Course.objects.get(course_name=course)
        what_to = WhatToKnow(course=cours,what_to_know=what_to_know)
        what_to.save()

    return redirect('teacherindex')

def add_whatwillyoulearn(request):
    if request.method == "POST":
        course = request.POST['course_select']
        what_you_will_learn = request.POST['what_you_will_learn']
        cours = Course.objects.get(course_name=course)
        what_you_will = WhatWillYouLearn(course=cours,what_to_learn=what_you_will_learn)
        what_you_will.save()

    return redirect('teacherindex')

def course_dashboard(request,name):
    course = Course.objects.get(course_name=name)
    topics = Topic.objects.filter(course=course)
    lessons = []
    for topic in topics:
        lesson = Lesson.objects.filter(topi=topic)
        lessons.append(lesson)
    context = {
        'course':course,
        'topics':topics,
        'lessons':lessons
    }
    return render(request,'course_dashboard.html',context)

def delete_topic(request,name):
    topic = Topic.objects.get(name=name)
    course = topic.course
    lessons = Lesson.objects.filter(topi=topic)
    lessons.delete()
    topic.delete()
    return redirect('course_dashboard',name=course.course_name)

def update_topic(request,name):
    topic = Topic.objects.get(name=name)
    course = topic.course
    if request.method == "POST":
        topic_name = request.POST['topic_name']
        topic.name = topic_name
        topic.save()

    return redirect('course_dashboard',name=course.course_name)

def delete_lesson(request,name):
    lesson = Lesson.objects.get(name=name)
    course = lesson.topi.course
    lesson.delete()
    return redirect('course_dashboard',name=course.course_name)

def update_lesson(request,name):
    lesson = Lesson.objects.get(name=name)
    course = lesson.topi.course
    if request.method == "POST":
        lesson_name = request.POST['lesson_name']
        myfile = True
        try:
            myfile = request.FILES['myfile']
        except:
            myfile = False
        if myfile:
            print("My file vitra")
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            lesson.video = filename
        else:
            pass
        lesson.name = lesson_name
        lesson.save()

    return redirect('course_dashboard',name=course.course_name)


@login_required
def enrollment(request,id):
    if request.method == "POST":
        student_user  = request.POST['student']
        usss =  use.objects.get(id=int(student_user))
        student = std.objects.get(user=usss)
        student.no_of_courses_enrolled += 1
        course = Course.objects.get(id=id)
        teacher = course.teacher
        teacher.no_of_enrolled_students += 1
        teacher.save()
        course.students.add(student)
        course.save()
        student.save()
    return redirect('index')

@login_required
def after_enrollment_course(request,name):
    course = Course.objects.get(course_name=name)
    topics = Topic.objects.filter(course=course)
    students_in_course = course.students.all()
    check = 0
    for student in students_in_course:
        if (student.user.id == request.user.id):
            check = 1
            break
        else:
            check = 0
    lessons = []
    context = {'course':course,'topics':topics}
    for topic in topics:
        lesson = Lesson.objects.filter(topi=topic)
        lessons.append(lesson)
    context.update({'lessons' : lessons})
    if check == 1:
        return render(request, 'coursesingle.html',context)
    else:
        return redirect('index')

@login_required
def course_list(request):
    user = request.user
    student = std.objects.get(user=user)
    courses = Course.objects.all()
    student_enrolled_courses = []
    for course in courses:
        stds = course.students.all()
        if student in stds:
            student_enrolled_courses.append(course)
    
    context = {
        'student_enrolled_courses':student_enrolled_courses,
        'student':student
    }

    return render(request, 'courses_list.html', context)