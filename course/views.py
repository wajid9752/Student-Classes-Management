from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,  logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from django.db.models import Max, F ,Count
from datetime import datetime , date , timedelta



@login_required(login_url="login")
def home(request):
    enrollments = Course_Enrolment.objects.all().order_by("student_id__student_name")
    for enrollment in enrollments:
        total_classes = enrollment.course_id.course_classes.count()
        remain_days = total_classes - int(  enrollment.enrol_course.count() ) 
        enrollment.end_date =  date.today() + timedelta(days=remain_days)
        enrollment.classes_num = total_classes
    
    return render(request , "home.html" , context={"students":enrollments})

@login_required(login_url="login")
def add_attendance(request,pk):
    obj=Course_Enrolment.objects.get(id=pk)
    if request.POST:
        get_id = request.POST.get("class_id")
        cls_obj=Course_Classes.objects.get(id=get_id)
        
        Attendance.objects.create(
            course_enrolment = obj ,
            attended_class = cls_obj ,
            student_id = obj.student_id ,
            attended_date = date.today()
        )
        messages.success(request , "Attendance Added Successfully")
        return redirect("/")

    class_to_attend = Course_Classes.objects.filter(course_id=obj.course_id)
    classes_dropdown = []
    for cd in class_to_attend:
        if not cd.id in [ at.attended_class.id for at in Attendance.objects.filter( student_id = obj.student_id) ]:
            classes_dropdown.append(cd)
    
    context={
        'classes_dropdown':classes_dropdown,
        'enroll': obj
    }
    return render(request , "add-attendance.html" , context)

##############################  Authentication ######################################

def user_login(request):    
    if request.POST:
        userName = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=userName, password=raw_password)
        if user is not None:
            login(request, user) 
            messages.success(request, "You are logged successfully.")
            return redirect("home")
        else:
            messages.error(request , "Credentials are not matched")
            return redirect("login")
        
    return render(request , "login.html")

def user_logout(request):
    logout(request)
    messages.success(request , "You are Logout Successfully!")
    return redirect("login")
