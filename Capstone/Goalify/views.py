from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Journal, Goal, Entries
from .forms import JournalForm, GoalForm, EntryForm
from datetime import datetime
current_time = datetime.now()

 # Create your views here.
def index(request):
     journals = Journal.objects.filter(user=request.user).all()
     if request.method == "POST":
          form = JournalForm(request.POST)
          if form.is_valid():
               new_journal = form.save()
               new_journal.journal_color = request.POST['journal_color']
               new_journal.journal_style = f"{new_journal.journal_color}.png"
               new_journal.journal_name = request.POST['journal_name']
               new_journal.user = request.user
               new_journal.save()
          return HttpResponseRedirect(reverse("index"))
     else:
          form = JournalForm         
          return render(request, 'goalify/index.html', {
               'form': form,
               'journals': journals
          })

def entry(request, journal_id):
     entries = Entries.objects.filter(journal_id=journal_id).all()
     journal = Journal.objects.get(id=journal_id)
     if request.method == "POST":
          formy = EntryForm(request.POST)
          if formy.is_valid():
               new_entry = formy.save()
               new_entry.user = request.user
               new_entry.journal = journal
               current_time = datetime.now()
               new_entry.date = current_time
               new_entry.save()
          return HttpResponseRedirect('#')
     else:
          formy = EntryForm
          return render(request, "goalify/entries.html", {
               'formy': formy,
               'entries': entries
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