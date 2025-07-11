from django.shortcuts import render,HttpResponse

# Create your views here.


def create_project(request):
   return render(request,"projects/create_projec.html") 

def join_projects(request):
   return render(request,"projects/join_project.html") 

def my_projects(request):
   return render(request,"projects/my_projects.html") 

def explore_projects(request):
   return render(request,"projects/explore_projects.html") 

def project_details(request):
   return render(request,"projects/project_details.html") 
