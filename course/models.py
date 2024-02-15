from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length = 100)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.course_name


class Course_Classes(models.Model):
    course_id = models.ForeignKey(  
                                    Course ,
                                    on_delete=models.CASCADE ,
                                    related_name = "course_classes"
                                     
                                      )
    class_name = models.CharField(max_length = 100)
    class_number = models.IntegerField()

    def __str__(self):
        return str(self.course_id.course_name) +": "+ str(self.class_number)
    
    class Meta:
        verbose_name = "Course Lecture Classes"

class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_class = models.CharField(max_length = 50)

    def __str__(self):
        return self.student_name
    



class Course_Enrolment(models.Model):
    course_id = models.ForeignKey(  
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    student_id = models.ForeignKey(  
        Student,
        on_delete=models.CASCADE,
        related_name="student_course"
    )

    class Meta:
        unique_together = ['course_id', 'student_id']
        verbose_name = "Student Course Enrolment"

    def __str__(self):
        return f"{self.course_id.course_name}: {self.student_id.student_name}"

class Attendance(models.Model):
    
    course_enrolment = models.ForeignKey(  
                                    Course_Enrolment ,
                                    on_delete=models.CASCADE ,
                                    related_name = "enrol_course"           
                                      )
    attended_class = models.ForeignKey(  
                                    Course_Classes ,
                                    on_delete=models.CASCADE ,
                                    related_name = "class_attendance"
                                     
                                      )
    student_id = models.ForeignKey(  
                                    Student ,
                                    on_delete=models.CASCADE ,
                                    related_name = "student_attendance"
                                     
                                      )
    remark = models.TextField(null=True , blank=True)
    attended_date = models.DateField()

    def __str__(self):
        return f"{self.course_enrolment.course_id.course_name}: {self.course_enrolment.student_id.student_name}"
    
    class Meta:
        verbose_name = "Student Course Wise Attendance"



    

    




    

    

    
    