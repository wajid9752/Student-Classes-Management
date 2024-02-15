
from django.contrib import admin
from .models import Course, Course_Classes, Student, Attendance,Course_Enrolment

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'start_date', 'get_students_count', 'get_classes_count')
    search_fields = ['course_name']
    list_filter = ['start_date']

    def get_students_count(self, obj):
        return obj.students.count()
    get_students_count.short_description = 'Students Count'

    def get_classes_count(self, obj):
        return obj.course_classes.count()
    get_classes_count.short_description = 'Classes Count'

admin.site.register(Course, CourseAdmin)


@admin.register(Course_Enrolment)
class Course_EnrolmentAdmin(admin.ModelAdmin):
    list_display = ['course_id','student_id']
    list_filter =['course_id','student_id']




class CourseClassesAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'course_name', 'class_number')
    search_fields = ['class_name']
    list_filter = ['course_id']

    def course_name(self, obj):
        return obj.course_id.course_name

admin.site.register(Course_Classes, CourseClassesAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_class')
    search_fields = ['student_name']
    
    

admin.site.register(Student, StudentAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'class_name','course', 'attended_date', 'remark')
    search_fields = ['student_id__student_name']
    list_filter = ['attended_date','course_enrolment__student_id' , 'course_enrolment__course_id']

    def student_name(self, obj):
        return obj.student_id.student_name

    def class_name(self, obj):
        return obj.attended_class.class_name
    
    def course(self, obj):
        return obj.course_enrolment.course_id.course_name
    

admin.site.register(Attendance, AttendanceAdmin)
