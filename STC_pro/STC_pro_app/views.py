from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import datetime
from STC_pro_app.models import Student,Teacher,Teacher_subject_model,Student_Assignment,Teacher_Assignment,Problem_solution,Rollnumber_Range,Teacher_id_Range,Running_subject,Tech_Notes_model,Notification_model
# Create your views here.
edit_id=1
stu_edit_id=1

def home_page_view(request):
        return render(request,'home.html')

def About_us_view(request):
        return render(request,'About_us.html')

def Contact_us_view(request):
        return render(request,'Contact_us.html')

def Logout_view(request):
        return redirect('/')

def Edit_student_view(request):
        if request.method=='POST':
            email = request.POST.get("e_mail")
            password = request.POST.get("passw")
            confirm_password = request.POST.get("conf_passw")
            contact = request.POST.get("mobile1")
            alternate_contact= request.POST.get("mobile2")
            addr = request.POST.get("dob")
            data=Student.objects.filter(user_id=edit_id)
            if password==confirm_password:
                if len(contact)==10 and len(alternate_contact)==10:
                    if contact!=alternate_contact:
                        data.update(password=password,contact=contact,alt_contact=alternate_contact,email=email)
                        messages.info(request,"* Your Profile is update successfully.")
                        return redirect('Edit_student')
                    else:
                        messages.info(request,"* Contact and alternate contact should be diffrent.")
                        return redirect('Edit_student')
                else:
                    messages.info(request,"* Please enter a valid Contact number")
                    return redirect('Edit_student')
            else:
                messages.info(request,"* Password and Confirm password are not matched.")
                return redirect('Edit_student')
        else:
            y=Student.objects.filter(user_id=stu_edit_id)
            di={}
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            for i in y:
                di={'subject_show':B,'fn':i.first_name,'ln':i.last_name,'uid':i.user_id,'em':i.email,'gen':i.gender,'pas':i.password,'con':i.contact,'alcon':i.alt_contact,'cou':i.course,'br':i.branch,'yr':i.year}
            return render(request,'Stu_Edit.html',context=di)


def Edit_view(request):
        if request.method=='POST':
            email = request.POST.get("e_mail")
            password = request.POST.get("passw")
            confirm_password = request.POST.get("conf_passw")
            contact = request.POST.get("mobile1")
            alternate_contact= request.POST.get("mobile2")
            addr = request.POST.get("dob")
            data=Teacher.objects.filter(user_id=edit_id)
            if password==confirm_password:
                if len(contact)==10 and len(alternate_contact)==10:
                    if contact!=alternate_contact:
                        data.update(password=password,contact=contact,alt_contact=alternate_contact,email=email)
                        messages.info(request,"* Your Profile is update successfully.")
                        return redirect('Edit')
                    else:
                        messages.info(request,"* Contact and alternate contact should be diffrent.")
                        return redirect('Edit')
                else:
                    messages.info(request,"* Please enter a valid Contact number")
                    return redirect('Edit')
            else:
                messages.info(request,"* Password and Confirm password are not matched.")
                return redirect('Edit')
        else:
            x=Teacher.objects.filter(user_id=edit_id)
            di={}
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            for i in x:
                di={'subject_show':B,'fn':i.first_name,'ln':i.last_name,'uid':i.user_id,'em':i.email,'gen':i.gender,'pas':i.password,'con':i.contact,'alcon':i.alt_contact,'add':i.Address,'cou':i.course,'br':i.branch,'yr':i.year}
            return render(request,'Edit.html',context=di)

def Tech_notification_view(request):
        if request.method=='POST':
            notification = request.POST.get("notification")
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            if not(Notification_model.objects.filter(Notification=notification).exists()):
                Notific=Notification_model.objects.create(Notification=notification,subject_noti=k)
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            C=Notification_model.objects.filter(subject_noti=k)
            return render(request,'Tech_notification.html',{'subject_show':B,'sbj':k,'notifications':C})
        else:
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            C=Notification_model.objects.filter(subject_noti=k)
            return render(request,'Tech_notification.html',{'subject_show':B,'sbj':k,'notifications':C})

def Tech_evaluation_view(request):
        a=request.GET.keys()
        k=''
        z=''
        for i in a:
            k=i
        D=Running_subject.objects.filter(subject_name=k)
        for i in D:
            z=i.year
        E=Student.objects.filter(year=z)
        B=Teacher_subject_model.objects.filter(subject_id=edit_id)
        return render(request,'Tech_evaluation.html',{'subject_show':B,'students':E,'sub':k})

def Check_Stu_Assignment_view(request):
        a=request.GET.keys()
        k=''
        z=''
        for i in a:
            k=i
        l=k.split()
        D=Running_subject.objects.filter(subject_name=l[0])
        for i in D:
            z=i.year
        E=Student.objects.filter(year=z)
        B=Teacher_subject_model.objects.filter(subject_id=edit_id)
        F=Student_Assignment.objects.filter(stu_id=l[-1],subject=l[0])
        return render(request,'Check_Stu_assignment.html',{'subject_show':B,'students':E,'sub':k,'stu_assign':F,'roll':l[-1]})

def Tech_solve_query_view(request):
        if request.method=='POST':
            que_id= request.POST.get("que_id")
            answer = request.POST.get("answer")
            ans_img = request.POST.get('ans_img')
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            data=Problem_solution.objects.filter(id=que_id)
            if ans_img and (not(Problem_solution.objects.filter(answer=answer).exists())):
                data.update(answer=answer,img_ans=ans_img)
            else:
                if (not(Problem_solution.objects.filter(answer=answer).exists())):
                    data.update(answer=answer)
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            C=Problem_solution.objects.filter(subject=k)
            return render(request,'Tech_solve_query.html',{'subject_show':B,'sbj':k,'questions':C})
        else:
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            C=Problem_solution.objects.filter(subject=k)
            return render(request,'Tech_solve_query.html',{'subject_show':B,'sbj':k,'questions':C})

def Stu_ask_query_view(request):
        if request.method=='POST':
            question = request.POST.get("question")
            que_img = request.POST.get('que_img')
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            if que_img and (not(Problem_solution.objects.filter(question=question).exists())) :
                data=Problem_solution.objects.create(question=question,img_que=que_img,subject=k)
            else:
                if (not(Problem_solution.objects.filter(question=question).exists())):
                    data=Problem_solution.objects.create(question=question,subject=k)
            A=Student.objects.filter(user_id=stu_edit_id)
            B=Running_subject.objects.filter(year=A[0].year)
            C=Problem_solution.objects.filter(subject=k)
            return render(request,'Stu_ask_query.html',{'subject_show':B,'sbj':k,'questions':C})
        else:
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            A=Student.objects.filter(user_id=stu_edit_id)
            B=Running_subject.objects.filter(year=A[0].year)
            C=Problem_solution.objects.filter(subject=k)
            return render(request,'Stu_ask_query.html',{'subject_show':B,'sbj':k,'questions':C})

def Tech_Assignment_view(request):
        if request.method=='POST':
            title = request.POST.get("title")
            assignment = request.POST.get("assign")
            assign_img = request.POST.get("assignment_img")
            last_date = request.POST.get("last_date")
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            if (not(Teacher_Assignment.objects.filter(assignment=assignment).exists())):
                Assignment_save=Teacher_Assignment.objects.create(subject=k,title=title,assignment=assignment,assign_img=assign_img,submittion_date=last_date)
            x=Teacher_Assignment.objects.filter(subject=k)
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            return render(request,'Tech_Assignment.html',{'subject_show':B,'Assignment':x,'sbj':k})
        else:
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            x=Teacher_Assignment.objects.filter(subject=k)
            B=Teacher_subject_model.objects.filter(subject_id=edit_id)
            return render(request,'Tech_Assignment.html',{'subject_show':B,'Assignment':x,'sbj':k})

def Stu_Assignment_view(request):
        if request.method=='POST':
            answer = request.POST.get('assign')
            assignment_no = request.POST.get('assignment_id')
            assign_img = request.POST.get("assignment_img")
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            if assign_img and (not(Student_Assignment.objects.filter(answer=answer).exists())):
                Assignment_save=Student_Assignment.objects.create(subject=k,stu_id=stu_edit_id,assignment_no=assignment_no,answer=answer,ans_img=assign_img)
            else:
                if (not(Student_Assignment.objects.filter(answer=answer).exists())):
                    Assignment_save=Student_Assignment.objects.create(subject=k,stu_id=stu_edit_id,assignment_no=assignment_no,answer=answer)
            x=Teacher_Assignment.objects.filter(subject=k)
            A=Student.objects.filter(user_id=stu_edit_id)
            z=0
            for i in A:
                z=i.year
            B=Running_subject.objects.filter(year=z)
            messages.info(request,"* Assignment is Submitted successfully")
            return render(request,'Stu_Assignment.html',{'subject_show':B,'Assignment':x,'sbj':k})
        else:
            a=request.GET.keys()
            k=''
            for i in a:
                k=i
            x=Teacher_Assignment.objects.filter(subject=k)
            A=Student.objects.filter(user_id=stu_edit_id)
            z=0
            for i in A:
                z=i.year
            B=Running_subject.objects.filter(year=z)
            return render(request,'Stu_Assignment.html',{'subject_show':B,'Assignment':x,'sbj':k})


def Tech_Notes_view(request):
    if request.method=='POST':
        title = request.POST.get("user")
        notes = request.POST.get("note")
        a=request.GET.keys()
        k=''
        for i in a:
            k=i
        notes_save=Tech_Notes_model.objects.create(subject=k,title=title,Notes=notes)
        x=Tech_Notes_model.objects.filter(subject=k)
        B=Teacher_subject_model.objects.filter(subject_id=edit_id)
        return render(request,'Tech_notes.html',{'subject_show':B,'notes':x,'sbj':k})
    else:
        a=request.GET.keys()
        k=''
        for i in a:
            k=i
        x=Tech_Notes_model.objects.filter(subject=k)
        B=Teacher_subject_model.objects.filter(subject_id=edit_id)
        return render(request,'Tech_notes.html',{'subject_show':B,'notes':x,'sbj':k})

def Stu_Notes_view(request):
        a=request.GET.keys()
        k=''
        for i in a:
            k=i
        x=Tech_Notes_model.objects.filter(subject=k)
        A=Student.objects.filter(user_id=stu_edit_id)
        B=Running_subject.objects.filter(year=A[0].year)
        return render(request,'Stu_notes.html',{'subject_show':B,'notes':x,'sb':k})

def Teacher_login_view(request):
            if request.method=='POST':
                user_id = request.POST.get("user")
                password = request.POST.get("password")
                global edit_id
                edit_id=user_id

                date=datetime.datetime.now()
                h=int(date.strftime('%H'))
                if h<12:
                    wish='Morning'
                elif h<16:
                    wish='AfterNoon'
                elif h<21:
                    wish='Evening'
                else:
                    wish='Night'
                if Teacher.objects.filter(user_id=user_id).exists():
                    x=Teacher.objects.filter(user_id=user_id)
                    name=x[0].first_name
                    B=Teacher_subject_model.objects.filter(subject_id=user_id)
                    for i in x:
                        if i.password==password:
                            return render(request,'welcom_techer.html',{'subject_show':B,'today_date':date,'msg':wish,'user_name':name})
                        else:
                            messages.info(request,"* Invalid Password")
                            return redirect('Teacher_login')
                else:
                    messages.info(request,"* Invalid User id")
                    return redirect('Teacher_login')
            else:
                return render(request,'Tech_login.html')

def Teacher_registration_view(request):
            if request.method=='POST':
                first_name = request.POST.get("f_name")
                last_name = request.POST.get("l_name")
                user_id = request.POST.get("U_id")
                email = request.POST.get("e_mail")
                gender = request.POST.get("gen")
                password = request.POST.get("passw")
                confirm_password = request.POST.get("conf_passw")
                contact = request.POST.get("mobile1")
                alternate_contact= request.POST.get("mobile2")
                addr = request.POST.get("dob")
                course = request.POST.get("cource")
                branch = request.POST.get("Branch")
                year = request.POST.get("Year")
                sub = request.POST.getlist("sub")
                first_name=first_name.strip()
                last_name=last_name.strip()
                C=Teacher_id_Range.objects.filter(branch=branch)
                if len(password)>=8:
                    j=0
                    for i in ["#","$","&","*","!","@","^","%"]:
                        j=j+1
                        if i in password:
                            break
                    if j!=len(password):
                        if password==confirm_password:
                            if Teacher.objects.filter(email=email).exists():
                                messages.info(request,"* Email is already taken.")
                                return redirect('Teacher_registration_view')
                            elif Teacher.objects.filter(user_id=user_id).exists():
                                messages.info(request,"* User id  is already taken.")
                                return redirect('Teacher_registration_view')
                            elif len(contact)==10 and len(alternate_contact)==10:
                                if contact!=alternate_contact:
                                    if first_name.isalpha():
                                        if last_name.isalpha():
                                            if len(C)!=0:
                                                if int(user_id)>=C[0].start and int(user_id)<=C[0].end:
                                                    data=Teacher.objects.create(first_name=first_name,last_name=last_name,user_id=int(user_id),email=email,gender=gender,password=password,contact=contact,alt_contact=alternate_contact,Address=addr,course=course,branch=branch,year=year)
                                                    for i in sub:
                                                        sub_data=Teacher_subject_model.objects.create(subject_id=user_id,subject=i)
                                                    return redirect('Teacher_login')
                                                else:
                                                    messages.info(request,"* Invalid User id")
                                                    return redirect('Teacher_registration_view')
                                            else:
                                                messages.info(request,"* Registration is not started yet")
                                                return redirect('Teacher_registration_view')
                                        else:
                                            messages.info(request,"* Last name should contain only aplphabates.")
                                            return redirect('Teacher_registration_view')
                                    else:
                                        messages.info(request,"* First name should contain only alphabates")
                                        return redirect('Teacher_registration_view')
                                else:
                                    messages.info(request,"* Contanct and alternate contact sould be diffrent")
                                    return redirect('Teacher_registration_view')
                            else:
                                messages.info(request,"* Contact should be 10 digit.")
                                return redirect('Teacher_registration_view')
                        else:
                            messages.info(request,"* Password and Confirm password are not matched.")
                            return redirect('Teacher_registration_view')
                    else:
                        messages.info(request,"* Password should consist of a special symbol.")
                        return redirect('Teacher_registration_view')
                else:
                    messages.info(request,"* Minimum length of password should be 8.")
                    return redirect('Teacher_registration_view')
            else:
                A=Running_subject.objects.all()
                return render(request,'Tech_reg.html',{'sub_list':A})

def Teacher_dashboard_view(request):
        return render(request,'Tech_dashboard.html')




def Student_login_view(request):
    if request.method=='POST':
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        global stu_edit_id
        stu_edit_id=user_id

        date=datetime.datetime.now()
        h=int(date.strftime('%H'))
        if h<12:
            wish='Morning'
        elif h<16:
            wish='AfterNoon'
        elif h<21:
            wish='Evening'
        else:
            wish='Night'
        Msg = Notification_model.objects.all()
        if Student.objects.filter(user_id=user_id).exists():
            x=Student.objects.filter(user_id=user_id)
            name=x[0].first_name
            B=Running_subject.objects.filter(year=x[0].year)
            for i in x:
                if i.password==password:
                    return render(request,'welcome_student.html',{'subject_show':B,'today_date':date,'msg':wish,'user_name':name,'d_noti':Msg})
                else:
                    messages.info(request,"* Invalid Password")
                    return redirect('Student_login')
        else:
            messages.info(request,"* Invalid User id")
            return redirect('Student_login')
    else:
        return render(request,'Stu_login.html')

def Student_registration_view(request):
    if request.method=='POST':
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        user_id = request.POST.get("U_id")
        email = request.POST.get("e_mail")
        gender = request.POST.get("gen")
        password = request.POST.get("passw")
        confirm_password = request.POST.get("conf_passw")
        contact = request.POST.get("mobile1")
        alternate_contact= request.POST.get("mobile2")
        DOB = request.POST.get("dob")
        course = request.POST.get("course")
        branch = request.POST.get("Branch")
        year = request.POST.get("Year")
        semester = request.POST.get("sem")
        first_name=first_name.strip()
        last_name=last_name.strip()
        a=int(year)
        C=Rollnumber_Range.objects.filter(year=a)
        if len(password)>=8:
            j=0
            for i in ["#","$","&","*","!","@","^","%"]:
                j=j+1
                if i in password:
                    break
            if j!=len(password):
                if password==confirm_password:
                    if Student.objects.filter(email=email).exists():
                        messages.info(request,"* Email is already taken.")
                        return redirect('Student_registration_view')
                    elif Student.objects.filter(user_id=user_id).exists():
                        messages.info(request,"* User id  is already taken.")
                        return redirect('Student_registration_view')
                    elif len(contact)==10:
                        if contact!=alternate_contact:
                            if first_name.isalpha():
                                if last_name.isalpha():
                                    if len(C)!=0:
                                        if int(user_id)>=C[0].start and int(user_id)<=C[0].end:
                                            data=Student.objects.create(first_name=first_name,last_name=last_name,user_id=int(user_id),email=email,gender=gender,password=password,contact=contact,alt_contact=alternate_contact,DOB=DOB,course=course,branch=branch,year=year)
                                            return redirect('Student_login')
                                        else:
                                            messages.info(request,"* Invalid Rollnumber")
                                            return redirect('Student_registration_view')
                                    else:
                                        messages.info(request,"* Registration is not started yet")
                                        return redirect('Student_registration_view')
                                else:
                                    messages.info(request,"* Last name should contain only aplphabates.")
                                    return redirect('Student_registration_view')
                            else:
                                messages.info(request,"* First name should contain only alphabates")
                                return redirect('Student_registration_view')
                        else:
                            messages.info(request,"* Contanct and alternate contact sould be diffrent")
                            return redirect('Student_registration_view')
                    else:
                        messages.info(request,"* Contact should be 10 digit.")
                        return redirect('Student_registration_view')
                else:
                    messages.info(request,"* Password and Confirm password are not matched.")
                    return redirect('Student_registration_view')
            else:
                messages.info(request,"* Password should consist of a special symbol.")
                return redirect('Student_registration_view')
        else:
            messages.info(request,"* Minimum length of password should be 8.")
            return redirect('Student_registration_view')
    else:
        return render(request,'Stu_reg.html')

def Student_dashboard_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        wish='Morning'
    elif h<16:
        wish='AfterNoon'
    elif h<21:
        wish='Evening'
    else:
        wish='Night'
    Msg = Notification_model.objects.all()
    x=Student.objects.filter(user_id=stu_edit_id)
    name=x[0].first_name
    A=Student.objects.filter(user_id=stu_edit_id)
    B=Running_subject.objects.filter(year=A[0].year)
    return render(request,'welcome_student.html',{'subject_show':B,'today_date':date,'msg':wish,'user_name':name,'d_noti':Msg})
