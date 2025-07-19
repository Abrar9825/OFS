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

<<<<<<< HEAD
urlpatterns = [    
        path('signup',views.signup,name="signup"),
        path('login',views.login,name="login"),
        path('forgotpassword',views.forgotpassword,name="forgotpassword"),
        path('github-auth',views.github_auth,name="github-auth"),
        path('profile',views.profile,name="profile"),
        path('edit_profile',views.edit_profile,name="edit_profile"),
=======
urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('forgotpassword', views.forgotpassword, name="forgotpassword"),
    path('github-auth', views.github_auth, name="github-auth"),
    path('profile', views.profile, name="profile"),
    path('set_new_password', views.set_new_password, name="set_new_password"),
>>>>>>> c3735eab91c10778443df3069180008bc651de07
]
