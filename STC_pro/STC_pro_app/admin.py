from django.contrib import admin
from STC_pro_app.models import Student,Teacher,Rollnumber_Range,Teacher_id_Range,Student_Assignment,Tech_Notes_model,Notification_model,Teacher_Assignment,Problem_solution,Teacher_subject_model,Computer_science_student,Mechanical_student,Electrical_student,Electronics_student,Running_subject

# Register your models here.
class Kit_subjects_admin(admin.ModelAdmin):
    list_display=['year','subject_code','subject_name']

class Rollnumber_Range_admin(admin.ModelAdmin):
    list_display=['year','start','end']

class Teacher_id_Range_admin(admin.ModelAdmin):
    list_display=['branch','start','end']

class Teacher_model_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','user_id','email','gender','contact','alt_contact','Address','course','branch','year']

class CSE_student_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','user_id','email','gender','contact','alt_contact','DOB','course','branch','year']
class ME_student_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','user_id','email','gender','contact','alt_contact','DOB','course','branch','year']
class EC_student_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','user_id','email','gender','contact','alt_contact','DOB','course','branch','year']
class EN_student_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','user_id','email','gender','contact','alt_contact','DOB','course','branch','year']

class Problem_solution_admin(admin.ModelAdmin):
    list_display=['subject','question','answer','img_ans','img_que']
class Teacher_Assignment_admin(admin.ModelAdmin):
    list_display=['subject','title','submittion_date','assignment','assign_img']
class Tech_Notes_model_admin(admin.ModelAdmin):
    list_display=['subject','title','Notes']
class Notification_model_admin(admin.ModelAdmin):
    list_display=['subject_noti','Notification']
class Student_Assignment_admin(admin.ModelAdmin):
    list_display=['subject','stu_id','assignment_no','answer','ans_img']



admin.site.register(Teacher_id_Range,Teacher_id_Range_admin)
admin.site.register(Rollnumber_Range,Rollnumber_Range_admin)
admin.site.register(Teacher,Teacher_model_admin)
admin.site.register(Running_subject,Kit_subjects_admin)
admin.site.register(Computer_science_student,CSE_student_admin)
admin.site.register(Mechanical_student,ME_student_admin)
admin.site.register(Electrical_student,EC_student_admin)
admin.site.register(Electronics_student,EN_student_admin)
admin.site.register(Problem_solution,Problem_solution_admin)
admin.site.register(Teacher_Assignment,Teacher_Assignment_admin)
admin.site.register(Tech_Notes_model,Tech_Notes_model_admin)
admin.site.register(Notification_model,Notification_model_admin)
admin.site.register(Student_Assignment,Student_Assignment_admin)
