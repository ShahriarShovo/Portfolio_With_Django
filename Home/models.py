from django.db import models

# Create your models here.

class Index(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_image', blank = True)
    twitter_url= models.URLField(max_length=2000, blank=True)
    facebook_url= models.URLField(max_length=2000, blank=True)
    instagram_url= models.URLField(max_length=2000, blank=True)
    github_url= models.URLField(max_length=2000, blank=True)
    linkedIn_url= models.URLField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.name

class Home(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home_image', blank = True)
    
class About(models.Model):
    summary = models.CharField (max_length=200, blank = True)
    image = models.ImageField(upload_to='home_image', blank = True)
    job_title = models.CharField (max_length=50, blank = True)
    job_summary = models.CharField (max_length=150, blank = True)
    birthday = models.DateField(max_length=20, blank = True)
    website = models.CharField (max_length=50, blank = True)
    phone = models.CharField (max_length=20, blank = True)
    city = models.CharField (max_length=50, blank = True)
    age = models.CharField (max_length=5, blank = True)
    degree = models.CharField (max_length=40, blank = True)
    email = models.CharField (max_length=25, blank = True)
    freelance =  models.CharField (max_length=20, blank = True)
    about_summary = models.CharField (max_length=500, blank = True)
    
    def __str__(self):
        return "About"
    
class Resume(models.Model):
    about_resume = models.CharField(max_length=300)
    name = models.CharField(max_length=30)
    about_myself = models.CharField(max_length=200)
    phone = models.CharField (max_length=20, blank = True)
    city = models.CharField (max_length=50, blank = True)
    email = models.CharField (max_length=25, blank = True)
    
    master_major_name =  models.CharField (max_length=50, blank = True)
    master_major_durations = models.CharField (max_length=15, blank = True)
    master_major_institute_name =  models.CharField (max_length=50, blank = True)
    about_master_institute =  models.CharField (max_length=150, blank = True)
    
    bachelor_major_name =  models.CharField (max_length=50, blank = True)
    bachelor_major_durations = models.CharField (max_length=15, blank = True)
    bachelor_major_institute_name =  models.CharField (max_length=50, blank = True)
    bachelor_master_institute =  models.CharField (max_length=150, blank = True)
    
    current_job_position_title =  models.CharField (max_length=50, blank = True)
    current_job_job_year = models.CharField (max_length=10, blank = True)
    current_job_job_city = models.CharField (max_length=25, blank = True)
    current_job_job_about = models.TextField(max_length=1000)
    
    old_job_position_title =  models.CharField (max_length=50, blank = True)
    old_job_job_year = models.CharField (max_length=10, blank = True)
    old_job_job_city = models.CharField (max_length=25, blank = True)
    old_job_job_about = models.TextField(max_length=1000) 
    
    def __str__(self):
        return "Resume"
    
class Services(models.Model):
    about_services = models.TextField(max_length=200, blank = True)
    
    service_1st = models.CharField(max_length=50, blank = True)
    about_service_1st = models.TextField(max_length=100, blank = True)
    
    service_2nd = models.CharField(max_length=50, blank = True)
    about_service_2nd = models.TextField(max_length=100, blank = True)
    
    service_3rd = models.CharField(max_length=50, blank = True)
    about_service_3rd = models.TextField(max_length=100, blank = True)
    
    def __str__(self):
        return "Services"
    
class Contact(models.Model):
    about_contact =  models.TextField(max_length=200, blank = True)
    phone = models.CharField (max_length=20, blank = True)
    city = models.CharField (max_length=50, blank = True)
    email = models.CharField (max_length=25, blank = True)
    
    def __str__(self):
        return "Contact"
    
    
    