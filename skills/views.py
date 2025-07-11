from django.shortcuts import render,HttpResponse

# Create your views here.


def skill_popup(request):
   return render(request,'skills/skill_popup.html') 

def skill_qa(request):
   return render(request,'skills/skill_qa.html') 

def skill_test_intro(request):
   return render(request,'skills/skill_test_intro.html') 

def skill_verification(request):
   return render(request,'skills/skill_verification.html') 

def test_result(request):
   return render(request,'skills/test_result.html') 

def test_fail(request):
   return render(request,'skills/test_fail.html') 
