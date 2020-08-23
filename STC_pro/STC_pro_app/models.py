from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_id=models.BigIntegerField(unique=True)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    alt_contact=models.BigIntegerField()
    DOB=models.CharField(max_length=35)
    course=models.CharField(max_length=25)
    branch=models.CharField(max_length=25)
    year=models.CharField(max_length=25)


class Teacher(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_id=models.BigIntegerField(unique=True)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    alt_contact=models.BigIntegerField()
    Address=models.CharField(max_length=35)
    course=models.CharField(max_length=25)
    branch=models.CharField(max_length=25)
    year=models.CharField(max_length=25)

class Teacher_subject_model(models.Model):
    subject_id=models.BigIntegerField()
    subject=models.CharField(max_length=50)

class Running_subject(models.Model):
    year=models.IntegerField()
    subject_code=models.CharField(max_length=10)
    subject_name=models.CharField(max_length=30)


class Teacher_Assignment(models.Model):
    subject=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    submittion_date=models.DateField()
    assignment=models.CharField(max_length=1000)
    assign_img=models.ImageField()

class Problem_solution(models.Model):
    subject = models.CharField(max_length=30)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000,null=True)
    img_ans = models.FileField(null=True)
    img_que = models.FileField(null=True)

class Tech_Notes_model(models.Model):
    subject = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    Notes = models.FileField()

class Notification_model(models.Model):
    subject_noti = models.CharField(max_length=30)
    Notification = models.CharField(max_length=100)

class Student_Assignment(models.Model):
    subject=models.CharField(max_length=30)
    stu_id = models.BigIntegerField()
    assignment_no = models.IntegerField()
    answer = models.CharField(max_length=1000)
    ans_img = models.FileField(null=True)


class Rollnumber_Range(models.Model):
    year=models.IntegerField()
    start=models.BigIntegerField()
    end=models.BigIntegerField()

class Teacher_id_Range(models.Model):
    branch=models.CharField(max_length=30)
    start=models.BigIntegerField()
    end=models.BigIntegerField()

class CSE_fillter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(branch="CSE")
class ME_fillter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(branch="ME")

class EC_fillter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(branch="EC")

class EN_fillter(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(branch="EN")


class Computer_science_student(Student):
    objects=CSE_fillter()
    class Meta:
        proxy=True
class Mechanical_student(Student):
    objects=ME_fillter()
    class Meta:
        proxy=True
class Electrical_student(Student):
    objects=EC_fillter()
    class Meta:
        proxy=True
class Electronics_student(Student):
    objects=EN_fillter()
    class Meta:
        proxy=True
