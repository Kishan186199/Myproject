"""STC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from STC_pro_app import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header='Admin Login'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home_page_view, name='Home'),
    url(r'about_us/',views.About_us_view),
    url(r'contact_us/',views.Contact_us_view),
    url(r'edit/',views.Edit_view, name='Edit'),
    url(r'home/',views.Logout_view),
    url(r'^Tech_notification/',views.Tech_notification_view,name='notification'),
    url(r'^Tech_solve_query/',views.Tech_solve_query_view),
    url(r'^Tech_evaluation/',views.Tech_evaluation_view),
    url(r'^Tech_Assignment/',views.Tech_Assignment_view),
    url(r'^Check_assignment/',views.Check_Stu_Assignment_view),
    url(r'^Stu_Assignment/',views.Stu_Assignment_view,name='stu_assignment'),
    url(r'^Tech_Notes/',views.Tech_Notes_view,name='Techer_notes'),
    url(r'^Stu_Notes/',views.Stu_Notes_view,name='Stu_notes'),
    url(r'^Tech_login/',views.Teacher_login_view, name='Teacher_login'),
    url(r'^Tech_reg/',views.Teacher_registration_view, name='Teacher_registration_view'),
    url(r'^Tech_dash/',views.Teacher_dashboard_view),
    url(r'^Stu_login/',views.Student_login_view, name='Student_login'),
    url(r'^Stu_reg/',views.Student_registration_view, name='Student_registration_view'),
    url(r'^Stu_dash/',views.Student_dashboard_view),
    url(r'edit_profile/',views.Edit_student_view, name='Edit_student'),
    url(r'^Stu_ask_query/',views.Stu_ask_query_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
