from django.shortcuts import render,HttpResponse

# Create your views here.


def core(request):
   return render(request,"core/contact.html") 

def landing_page(request):
   return render(request,"core/landing_page.html") 
