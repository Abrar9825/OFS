"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
        path('create-projects',views.create_project,name="create-project"),
        path('join-projects',views.join_projects,name="join-projects"),
        path('my-projects',views.my_projects,name="my-projects"),
        path('explore-projects',views.explore_projects,name="explore-projects"),
        path('project-details',views.project_details,name="project-details"),
]
