from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Journal, Goal, Entries, Timer, History
from .forms import JournalForm, GoalForm, EntryForm, TimerForm, ProgressForm
from datetime import datetime, date
from django.utils import timezone
import json
current_time = datetime.now()

 # Create your views here.
def index(request):
     goals = Goal.objects.filter(user=request.user).all().order_by('-date').all()
     journals = Journal.objects.filter(user=request.user).all().order_by('-journal_date').all()
     if request.method == "POST":
          formo = GoalForm(request.POST)
          form = JournalForm(request.POST)
          if form.is_valid():
               new_journal = form.save()
               new_journal.journal_color = request.POST['journal_color']
               new_journal.journal_style = f"{new_journal.journal_color}.png"
               new_journal.journal_name = request.POST['journal_name']
               timey = datetime.now()
               new_journal.journal_date = timey
               new_journal.user = request.user
               new_journal.save()
               return HttpResponseRedirect(reverse("index"))
          if formo.is_valid():
               new_goal = formo.save()
               new_goal.user = request.user
               new_goal.name = request.POST['name']
               new_goal.goal_time = request.POST['goal_time']
               new_goal.frequency = request.POST['frequency']
               new_goal.progress_start = 0
               new_goal.progress_total = request.POST['frequency']
               timey = datetime.now()
               new_goal.date = timey
               new_goal.save()
               Timer.objects.create(id=new_goal.id, time=new_goal.goal_time)
               return HttpResponseRedirect(reverse("index"))
     else:
          formo = GoalForm
          form = JournalForm         
          return render(request, 'goalify/index.html', {
               'form': form,
               'formo': formo,
               'journals': journals,
               'goals': goals
          })

def entry(request, journal_id):
     entries = Entries.objects.filter(journal_id=journal_id).all().order_by('-date')
     journals = Journal.objects.get(id=journal_id)
     if request.method == "POST":
          formy = EntryForm(request.POST)
          if formy.is_valid():
               new_entry = formy.save()
               new_entry.user = request.user
               new_entry.journal = journals
               current_time = timezone.now()
               new_entry.date = current_time
               new_entry.save()
          return HttpResponseRedirect('#')
     else:
          p = Paginator(entries, 1)
          page_number = request.GET.get('page')
          try:
            page_obj = p.get_page(page_number)
          except PageNotAnInteger:
            page_obj = p.page(1)
          except EmptyPage:
            page_obj = p.page(p.num_pages)
          formy = EntryForm
          return render(request, "goalify/entries.html", {
               'page_obj': page_obj,
               'formy': formy,
               'entries': entries,
               'journals': journals.journal_name,
               'p': p
          })

def timer(request, timer_id):
          if request.method == "POST":
               goal = Goal.objects.filter(id=timer_id)
               goal_progress = goal.values_list('progress_start', flat=True)[0]
               new_goal = goal_progress + 1
               proform = ProgressForm(request.POST)
               if proform.is_valid():
                    Goal.objects.filter(id=timer_id).update(progress_start=new_goal)
               return redirect("index")
          else:
               goals = Goal.objects.filter(id=timer_id).all()
               proform = ProgressForm
               times = Timer.objects.filter(id=timer_id).all()
               clock = times.values_list('time', flat=True)[0]
               moving_time = "00:00"
               return render(request, "goalify/timer.html", {
                    'goals': goals,
                    'proform': proform,
                    'times': times,
                    'clock': clock,
                    'moving_time': moving_time
               })
     

def history(request):
     history = History.objects.filter(user=request.user).all().order_by('-date').all()
     if request.method == "POST":
          name = request.POST['name']
          time = request.POST['time']
          frequency = request.POST['frequency']
          id = request.POST['id']
          date_str = current_time
          formatted_date = date_str.strftime("%Y-%m-%d %H:%M:%S.%f%z")
          History.objects.create(user=request.user, name=name, goal_time=time, frequency=frequency, date=formatted_date)
          goal_gone = Goal.objects.filter(id=id).all()
          goal_gone.delete()
          return HttpResponseRedirect('#')
     else:
          return render(request, "goalify/history.html", {
               'history': history
          })

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