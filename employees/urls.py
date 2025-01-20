from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.logins, name='logins'),
    path('homepg/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('logins', views.logins, name='logins'),
    path('sign', views.signin, name='sign'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('list/', views.employees, name='employees'),
    path('attendance', views.attendances, name='attendaces'),
    path('attendance_list', views.attendance_register, name='attendancelist'),
    path('payroll/', views.payroll, name='payroll'),
    path('attendanceRec/', views.attendace_record, name='attendanceRec'),
    path('logout', views.custom_logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('report/', views.report, name='reports'),
    path('mail/', views.mail, name='mail'),
    path('create_task', views.create_task, name='task'),
    path('feed/', views.feed, name='feeds'),
    path('create/', views.task, name='create'),
    path('add_comment/<int:task_id>/', views.add_comment, name='add_comment'),
    path('employee/edit/<int:id>/', views.edit_profile, name='edit'),
    path('employee/documentupdtate/<int:id>/', views.update, name='update'),
    path('leader/', views.leader, name='leader'),
    path('leder/delete-employee/<int:id>/', views.delete_attendance, name='delete_attendance'),
    path('adminattendance/', views.adminattendance, name='adminattendance'),
    path('employeelist/', views.employee_list, name='employeelist'),
    path('leader/delete-employee/<int:id>/', views.delete_employee, name='delete_employee'),
    path('admin_register/', views.admin_register, name='register_admin'),
    path('send-reset-link/', views.send_reset_link, name='send_reset_link'),
    path("reset-password/<str:token>/", views.reset_password, name="reset_password"),




  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
