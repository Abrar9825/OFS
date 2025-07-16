from django.shortcuts import render,HttpResponse

# Create your views here.


def leaderboard(request):
   return render(request,"leaderboard/leaderboard.html") 
