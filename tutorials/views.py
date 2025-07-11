from django.shortcuts import render,HttpResponse

# Create your views here.


def tutorials(request):
   return render(request,"tutorials/tutorial.html") 
