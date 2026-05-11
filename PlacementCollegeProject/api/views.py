from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import StudentProfile, CompanyProfile
from .models import Job
from django.contrib.auth.decorators import login_required 


# 1. FIXED REGISTER VIEW FOR HTML FORMS
# Replace your old register function with this:
def register(request):
    if request.method == "POST":
        u_type = request.POST.get('user_type')
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        u_pass = request.POST.get('password')
        
        # 1. Create the Base User
        new_user = User.objects.create_user(username=u_name, email=u_email, password=u_pass)
        
        # 2. Handle Student Registration
        if u_type == "student":
            StudentProfile.objects.create(
                user=new_user,
                phone=request.POST.get('phone'),
                course=request.POST.get('course'),
                percentage=request.POST.get('percentage') or 0,
                skills=request.POST.get('skills'),
                resume=request.FILES.get('resume')
            )
        elif u_type == "company":
            CompanyProfile.objects.create(
                user=new_user,
                company_name=request.POST.get('company_name'), # Must match HTML name
                phone=request.POST.get('phone'),               # Matches your models.py
                website=request.POST.get('website', ''),
                industry=request.POST.get('industry', 'IT')
            )

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')
    
    return render(request, 'register.html')
        

# 2. FIXED LOGIN VIEW FOR HTML FORMS
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # 1. Find the user by email first
        try:
            target_user = User.objects.get(email=email_input)
            # 2. Authenticate using their actual username
            user = authenticate(request, username=target_user.username, password=password_input)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            print(f"Status: Login Successful for {user_type}!")
            
            # 3. Redirect based on the dropdown choice
            if user_type == "admin":
                return redirect('admin:index')
            elif user_type == "company":
                return redirect('company_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            print("Status: Authentication Failed")
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


# def login_view(request):
#     if request.method == "POST":
#         # 1. Capture the data
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type')

#         # 2. Debug print
#         print(f"--- Login Attempt (Bypass Mode) ---")
#         print(f"Email: {email} | Type: {user_type}")

#         # 3. Direct Navigation (Bypassing database for now)
#         if user_type == "admin":
#             return redirect('admin_dashboard')
#         elif user_type == "company":
#             return redirect('company_dashboard')
#         else:
#             # This handles 'student'
#             return redirect('student_dashboard')

#     return render(request, 'login.html')


#3.update api/views.py
def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')

#4. Student module functions
@login_required
def student_dashboard(request):
    return render(request, 'student-dashboard.html')

def student_profile(request):
    return render(request, 'student-profile.html')

def student_jobs(request):
    return render(request, 'student-jobs.html')

def student_applied(request):
    return render(request, 'student-applied.html')


#5. Admin module functions
@login_required
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_add_jobs(request):
    return render(request, 'admin-add-jobs.html')

def admin_manage_students(request):
    return render(request, 'admin-manage-students.html')

#6. Company module functions
@login_required
def company_dashboard(request):
    return render(request, 'company-dashboard.html')

def company_post_jobs(request):
    return render(request, 'company-post-jobs.html')

def company_applicants(request):
    return render(request, 'company-applicants.html')

#7. logout redirecting to index/home  page
def logout_view(request):
    auth_logout(request)
    return redirect('index')

def home(request):
    jobs_from_db = Job.objects.all().order_by('-id')
    print(f"DEBUG: Found {jobs_from_db.count()} jobs in database")
    return render(request, 'index.html',{'jobs':jobs_from_db})
