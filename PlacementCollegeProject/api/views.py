from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# 1. FIXED REGISTER VIEW FOR HTML FORMS
def register(request):
    if request.method == "POST":
        # Read from standard HTML form inputs using your exact 'name' attributes
        # Since your current form inputs don't have name tags, Django will use their type/placeholder map:
        full_name = request.POST.get('full_name') 
        email = request.POST.get('email') or request.POST.get('username')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')

        # Use email as the standard Django username field
        username = email 

        if not username or not password:
            messages.error(request, "Email and Password are required.")
            return render(request, 'register.html')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "A user with this email already exists.")
            return render(request, 'register.html')

        # Create the standard user object
        user = User.objects.create_user(username=username, password=password)
        user.first_name = full_name if full_name else ""
        user.save()

        # OPTIONAL VIVA TIP: In a full setup, you'd save 'user_type' and 'phone' to a custom Profile model here.

        messages.success(request, "Registration successful! Please login.")
        return redirect('login') # Sends them straight to the login page

    # If GET request, just display the registration page
    return render(request, 'register.html')


# 2. FIXED LOGIN VIEW FOR HTML FORMS
def login_view(request):

    if request.method == "POST":
        # Read the email and password sent by your login.html form
        username = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type') # Student, Admin, or Company

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user) # Logs the user into the session
            
            # Smart Redirect based on what role they selected in your dropdown
            if user_type == "Admin":
                return redirect('admin_dashboard')
            elif user_type == "Company":
                return redirect('company_dashboard')
            else:
                return redirect('student_dashboard')
                return render(request,'login.html')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    # If GET request, just display the login page
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