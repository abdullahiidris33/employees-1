from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee,Attendance,Payroll,Task,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import uuid



# Create your views here.


@login_required
def home(request):
    employee = Employee.objects.get(user = request.user)
    return render(request, 'employees/index.html', {'employee': employee })

def signup(request):
    return render(request, 'employees/Signup.html')

def admin_dashboard(request):
    employee = Employee.objects.all()
    return render(request, 'employees/admin.html', {'employee': employee})

def employees(request):
    employee = Employee.objects.all()
    

    return render(request, 'employees/list.html', {'employee': employee })

def attendances(request):
    employee = Employee.objects.all()
    attendance = Attendance.objects.all()

    return render(request, 'employees/attendance.html', {'attendance': attendance, 'employee': employee})

def attendace_record(request):
    attendance = Attendance.objects.all()

    return render(request, 'employees/attendencelist.html', {'attendance': attendance})

def payroll(request):
    payment = Payroll.objects.all()
    return render(request, 'employees/payroll.html', {'payment': payment})


def edit_profile(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employees/edit.html', {'employee': employee} )



def update(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        employee.first_name = first_name
        employee.last_name = last_name
        employee.email = email
        employee.phone_number = phone_number

        if 'profile_picture' in request.FILES:
            employee.profile_picture = request.FILES['profile_picture']

        employee.save()
        return redirect('profile')

    return render(request, 'employees/update_profile.html', {'employee': employee})
   


def report(request):
    return render(request, 'employees/report.html')




def mail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages_content = request.POST.get('messages')

        subject = f"Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{messages_content}"

        try:
            send_mail(
                subject=subject,
                message=message_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['rprogrammer25@gmail.com', 'programmingwwithcoys@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message was sent successfully!")
            return redirect('home')
        except Exception as e:
            print(f"Error: {e}")  
            messages.error(request, "Failed to send your message. Please try again.")
            return redirect('home')

    return redirect('reports')



def attendance_register(request):
    if request.method == "POST":
        employee_id = request.POST['employee']
        date = request.POST['date']
        status = request.POST['status']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']


        employee = get_object_or_404(Employee, id=employee_id)

        new_attendance = Attendance(
            employee=employee,
            date=date,
            status=status,
            check_in=check_in,
            check_out=check_out
        )
        new_attendance.save()

        messages.success(request, "Attendance has been submitted successfully!")
        return redirect('home')

    return redirect('attendaces')


@login_required
def create_task(request):
    employee = Employee.objects.get(user=request.user)

    if request.method == "POST":
        task_title = request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        new_task = Task(
            employee=employee, 
            task_title=task_title,
            task_description=task_description,
            due_date=due_date,
            priority=priority,
        )
        new_task.save()
        return redirect('feeds')



    return render(request, 'employees/feed.html', {'employee': employee})




def task(request):
    create = Task.objects.all()
    return render(request, 'employees/task.html', {'create': create})


def add_comment(request, task_id):
    if request.method == "POST":
        text = request.POST.get('text')
        task = get_object_or_404(Task, id=task_id)

        Comment.objects.create(
            task=task,
            author=request.user,  
            text=text,
        )

        return redirect('feeds')

    return redirect('home') 


def feed(request):
    tasks = Task.objects.prefetch_related('comments').all()
    employee = Employee.objects.get(user=request.user) 
    return render(request, 'employees/feed.html', {'tasks': tasks, 'employee': employee})





def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone_number = request.POST['phone_number']
        country = request.POST['country']
        profile_picture = request.FILES.get('profile_picture')

        if password != confirm_password:
            return redirect('signup')
        
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        employee = Employee(
            user=user,
            first_name = first_name,
            last_name=last_name,
            email=email,
            password=password,
            username=username,
            confirm_password=confirm_password,
            phone_number=phone_number,
            country=country,
            profile_picture=profile_picture
        )

        employee.save()

        return redirect('login')
    return render(request, 'employees/index.html')

def logins(request):
    return render(request, 'employees/login.html')
def leader(request):
    return render(request, 'employees/leader.html')



def profile(request):
    employee = Employee.objects.get(user = request.user)
    return render(request, 'employees/profile.html', {'employee': employee })

def custom_logout_view(request):
    logout(request)
    return redirect('logins')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if username == 'mrsoja4' and password == '$Ss2119612598':
                return redirect('leader')

            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('logins')

    return render(request, 'employees/login.html')

def adminattendance(request):   
    attendance = Attendance.objects.all()

    return render(request, 'employees/adminattendance.html', { 'attendance': attendance })

def employee_list(request):
    employee = Employee.objects.all()

    return render(request, 'employees/employeelist.html', {'employee': employee})


def delete_attendance(request, id):
    attendance = get_object_or_404(Attendance, id=id)

    if request.method == 'POST':
        attendance.delete()
        messages.success(request, "Attendance record deleted successfully!")
        return redirect('adminattendance')
    
    return render(request, 'employees/confirm_delete.html', {'attendance': attendance})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employeelist')
    return redirect('home')

def admin_register(request):
    return render(request, 'employees/admin_register.html')



def send_reset_link(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            employee = Employee.objects.get(email=email)
        except Employee.DoesNotExist:
            messages.error(request, "Email not found.")
            return redirect('send_reset_link')

        reset_token = str(uuid.uuid4())
        employee.reset_token = reset_token
        employee.save()

        reset_url = request.build_absolute_uri(f"/reset-password/{reset_token}/")
        send_mail(
            'Reset Your Password',
            f'Click the link below to reset your password:\n{reset_url}',
            'admin@example.com',
            [email],
        )

        messages.success(request, "Password reset link has been sent to your email.")
        return redirect('logins')

    return render(request, 'employees/send_reset_link.html')



def reset_password(request, token):
    try:
        employee = Employee.objects.get(reset_token=token)
    except Employee.DoesNotExist:
        messages.error(request, "Invalid or expired reset token.")
        return redirect("send_reset_link")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            employee.password = password
            employee.reset_token = None  
            employee.save()

            if employee.user:
                user = employee.user
                user.set_password(password)
                user.save()
            messages.success(request, "Password updated successfully.")
            return redirect("logins")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "employees/reset_password.html", {"employee": employee})



















