from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Employee,Attendance, Payroll,Comment,Task


# Customizing the Admin Interface for Employee
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'email', 'country', 'hire_date', 'profile_picture', 'phone_number')  # Fields to display in the list view
#     list_filter = ('country', 'hire_date')  # Add filters for country and hire date
#     search_fields = ('first_name', 'last_name', 'email', 'username')  # Enable search functionality
#     ordering = ('hire_date',)  # Default ordering by hire date
#     readonly_fields = ('hire_date',)  # Make hire date read-only
#     fieldsets = (
#         ("Personal Information", {
#             "fields": ('first_name', 'last_name', 'email', 'phone_number', 'country', 'profile_picture'),
#         }),
#         ("Account Information", {
#             "fields": ('username', 'password', 'confirm_password'),
#         }),
#         ("Important Dates", {
#             "fields": ('hire_date',),
#         }),
#     )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_first_name', 'get_last_name', 'get_email', 'country', 'hire_date', 'profile_picture', 'phone_number')  # Updated fields
    list_filter = ('country', 'hire_date')  # Add filters for country and hire date
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'username')  # Enable search functionality for User fields
    ordering = ('hire_date',)  # Default ordering by hire date
    readonly_fields = ('hire_date',)  # Make hire date read-only
    fieldsets = (
        ("Personal Information", {
            "fields": ('get_first_name', 'get_last_name', 'get_email', 'phone_number', 'country', 'profile_picture'),
        }),
        ("Account Information", {
            "fields": ('username', 'password', 'confirm_password'),
        }),
        ("Important Dates", {
            "fields": ('hire_date',),
        }),
    )

    # Methods to access User fields
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'




class AttendanceAdmin(admin.ModelAdmin):
        
    Attendance_display = ('employee','date', 'status')

class PayrollAdmin(admin.ModelAdmin):
    payment_list = ('employee', 'salary', 'allowances', 'deducations', 'net_paid', 'payment_date', 'payment_status')

class CommentAdmin(admin.ModelAdmin):
    comment_list = ('comment')

class TaskAdmin(admin.ModelAdmin):
    task = ('employee', 'task_title', 'task_description', 'due_date', 'priority' )

# Registering the Employee model with the custom admin view
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Payroll,PayrollAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Task,TaskAdmin)


