from django.db import models
from django.contrib.auth.models import User

# 1. Student Profile (Handles Resume Uploads)
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    # Uploads to a 'resumes/' folder in your media directory
    resume = models.FileField(upload_to='resumes/', null=True, blank=True) 
    skills = models.TextField(help_text="Enter skills separated by commas")

    def __str__(self):
        return self.user.username

# 2. Company Profile
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, default="IT")
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.company_name

# 3. Job Table (With Eligibility Criteria)
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    min_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company.company_name}"

# 4. Application Table (The "Naukri" Engine)
class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.student.user.username} applied for {self.job.title}"