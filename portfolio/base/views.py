from django.shortcuts import render
from .models import Profile, SocialLink, Project, Hobby

def home(request):
    profile = Profile.objects.first()
    socials = SocialLink.objects.all()
    projects = Project.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, "base/home.html", {
        "profile": profile,
        "socials": socials,
        "projects": projects,
        "hobbies": hobbies,
    })
