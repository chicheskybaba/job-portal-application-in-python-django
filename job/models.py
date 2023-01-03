
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class StudentUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=15,null=True)
    typ=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username
        
        

class Recruiter(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=15,null=True)
    company=models.CharField(max_length=15,null=True)
    typ=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username



class Job(models.Model):
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    company=models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    salary=models.IntegerField()
    desc=models.TextField(max_length=500)
    location=models.CharField(max_length=50)
    date_posted=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.title
    
              
        

class Applicant(models.Model):
    name=models.CharField(max_length=100)
    applied_job=models.ForeignKey(Job,on_delete=models.CASCADE)
    skills=models.CharField(max_length=200)
    mobile=models.IntegerField()
    address=models.CharField(max_length=150, default='Enter your Address')
    coverletter=models.TextField(max_length=2000, null=True)
    cv = models.FileField(upload_to='cvs', blank=True, null=True)
    

