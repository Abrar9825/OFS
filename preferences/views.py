from django.shortcuts import render,HttpResponse

# Create your views here.


def preferences(request):
   return render(request,'preferences/preference_page.html')
