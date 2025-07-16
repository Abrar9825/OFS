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
        path('skill-qa',views.skill_qa,name="skill-qa"),
        path('skill-test-intro',views.skill_test_intro,name="skill-test-intro"),
        path('skill-verification',views.skill_verification,name="skill-verification"),
        path('test-result',views.test_result,name="test-result"),
        path('test-fail',views.test_fail,name="test-fail"),
]
