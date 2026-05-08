from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# 1. FIXED REGISTER VIEW FOR HTML FORMS
# Replace your old register function with this:
def register(request):
    if request.method == "POST":
        u_type = request.POST.get('user_type')
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        u_pass = request.POST.get('password')
        
        # 1. Create the base User
        new_user = User.objects.create_user(username=u_name, email=u_email, password=u_pass)

        # 2. Logic based on User Type
        if u_type == "student":
            StudentProfile.objects.create(
                user=new_user,
                phone=request.POST.get('phone'),
                course=request.POST.get('course'),
                percentage=request.POST.get('percentage') or 0,
                skills=request.POST.get('skills'),
                resume=request.FILES.get('resume') # Handles the PDF
            )
        elif u_type == "company":
            CompanyProfile.objects.create(
                user=new_user,
                company_name=u_name, # Using username as default company name
                contact_number=request.POST.get('phone')
            )

        messages.success(request, "Registration successful! Please login.")
        return redirect('login')

    return render(request, 'register.html')

# 2. FIXED LOGIN VIEW FOR HTML FORMS
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# def login_view(request):
#     if request.method == "POST":
#         # 1. Capture data from the HTML form names
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type')

#         # 2. Debug: This shows up in your VS Code terminal
#         print(f"--- Login Attempt ---")
#         print(f"Email: {email} | Type: {user_type}")

#         # 3. Try to find the user in the database
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             auth_login(request, user)
#             print("Status: Login Successful!")
            
#             # 4. Redirect based on the dropdown choice
#             if user_type == "admin":
#                 return redirect('admin_dashboard')
#             elif user_type == "company":
#                 return redirect('company_dashboard')
#             else:
#                 return redirect('student_dashboard')
#         else:
#             print("Status: Authentication Failed")
#             messages.error(request, "Invalid email or password.")
#             return render(request, 'login.html')

#     # If someone just visits the page (GET request)
#     return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        # 1. Capture the data
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # 2. Debug print
        print(f"--- Login Attempt (Bypass Mode) ---")
        print(f"Email: {email} | Type: {user_type}")

        # 3. Direct Navigation (Bypassing database for now)
        if user_type == "admin":
            return redirect('admin_dashboard')
        elif user_type == "company":
            return redirect('company_dashboard')
        else:
            # This handles 'student'
            return redirect('student_dashboard')

    return render(request, 'login.html')


#3.update api/views.py
def index(request):
    return render(request,'index.html')


#4. Student module functions
def student_dashboard(request):
    return render(request, 'student-dashboard.html')

def student_profile(request):
    return render(request, 'student-profile.html')

def student_jobs(request):
    return render(request, 'student-jobs.html')

def student_applied(request):
    return render(request, 'student-applied.html')


#5. Admin module functions
def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def admin_add_jobs(request):
    return render(request, 'admin-add-jobs.html')

def admin_manage_students(request):
    return render(request, 'admin-manage-students.html')

#6. Company module functions
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