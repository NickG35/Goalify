from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Journal, Goal
from .forms import JournalForm, GoalForm
from datetime import datetime

 # Create your views here.
def index(request):
     journals = Journal.objects.all()
     if request.method == "POST":
          form = JournalForm(request.POST)
          if form.is_valid():
               new_journal = form.save()
               new_journal.user = request.user
               new_journal.save()
          return HttpResponseRedirect('#')
     else:
          form = JournalForm         
          return render(request, 'goalify/index.html', {
               'form': form,
               'journals': journals
          })

def history(request):
     return render(request, "goalify/history.html")

def login_view(request):
     if request.method == "POST":

          # attempt to sign user in
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request, username=username, password=password)

          if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse("index"))
          else:
               return render(request, "goalify/login.html", {
                    "message": "Invalid username and/or password."
               })
     else:
          return render(request, "goalify/login.html")

def logout_view(request):
     logout(request)
     return render(request, "goalify/login.html")

def register(request):
     if request.method == "POST":
          username = request.POST["username"]
          email = request.POST["email"]

          password = request.POST["password"]
          confirmation = request.POST["confirmation"]
          if password != confirmation:
               return render(request, "goalify/index.html", {
                    "message": "Passwords do not match"
               })
          
          try:
               user = User.objects.create_user(username, email, password)
               user.save()
          except IntegrityError:
               return render(request, "goalify/register.html", {
                    "message": "Username already taken."
               })
          login(request, user)
          return HttpResponseRedirect(reverse("index"))
     else:
          return render(request,"goalify/register.html")