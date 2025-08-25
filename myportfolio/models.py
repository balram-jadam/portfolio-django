from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    # website = models.URLField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)  # Could use choices
    description = models.TextField()
    myimage = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Skill(models.Model):
    skillname = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    desc = models.TextField( null=True, blank=True)
    
    def __str__(self):
        return self.skillname
    

class ResumeAbout(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class ResumeProjects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title
    
class ResumeEducation(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    start_year = models.PositiveIntegerField()
    ending_year = models.PositiveIntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return self.degree
    
class ResumeLanguages(models.Model):
    languages = models.CharField(max_length=100)
    
    def __str__(self):
        return self.languages
    
class ResumeFrameworks(models.Model):
    frameworks = models.CharField(max_length=100)
    
    def __str__(self):
        return self.frameworks
    
class ResumeDatabase(models.Model):
    database = models.CharField(max_length=100)
    
    def __str__(self):
        return self.database
    
class ResemeTools(models.Model):
    tools = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tools
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"