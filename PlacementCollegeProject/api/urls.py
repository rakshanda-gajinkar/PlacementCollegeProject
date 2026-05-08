from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/jobs/', views.student_jobs, name='student_jobs'),
    path('student/applied/', views.student_applied, name='student_applied'),
    
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add-jobs/', views.admin_add_jobs, name='admin_add_jobs'),
    path('admin/manage-students/', views.admin_manage_students, name='admin_manage_students'),

    path('company/dashboard/', views.company_dashboard, name='company_dashboard'),
    path('company/applicants/', views.company_applicants, name='company_applicants'),
    path('company/post-job/', views.company_post_jobs, name='company_post_jobs'),

    path('logout/', views.logout_view, name='logout'),
]