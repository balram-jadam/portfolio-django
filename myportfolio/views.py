from django.shortcuts import render,redirect
from django.contrib import messages
from .models import About,Skill,ResumeAbout,ResumeDatabase,ResemeTools,ResumeEducation,ResumeFrameworks,ResumeLanguages,ResumeProjects,Contact

# Create your views here.

def show(request):
    about= About.objects.first()
    skills=Skill.objects.all()
    resumeabout = ResumeAbout.objects.all()
    databases = ResumeDatabase.objects.all()
    education = ResumeEducation.objects.all()
    frameworks = ResumeFrameworks.objects.all()
    Projects = ResumeProjects.objects.all()
    languages = ResumeLanguages.objects.all()
    tools = ResemeTools.objects.all()
    
    if request.method=="POST":
        name  = request.POST['name']
        email  = request.POST['email']
        subject  = request.POST['subject']
        message  = request.POST['message']
        
        fm = Contact(name=name,email=email,subject=subject,message=message)
        # messages.success(request,'Your message has been sent. Thank you!')
        fm.save()
        # return redirect('/')
        
    
    return render(request,'index.html',{'about':about,'skills':skills,'resumeabout':resumeabout,'Projects':Projects,'databases':databases,'education':education,'frameworks':frameworks,'languages':languages,'tools':tools})


def resume_views(request):
    return render(request,'index.html')


    
    

