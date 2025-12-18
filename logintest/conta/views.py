from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginview(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=user, password=password)
        if user is not None:
          login(request, user)
          return redirect("home")
        else:
         return render(request, "loginpage.html", {"error": "invalid login"})
    return render(request, "login.html")

def logoutview(request):
   logout(request)
   return redirect("login")

@login_required
def home(request):
   return render(request,"home.html")
