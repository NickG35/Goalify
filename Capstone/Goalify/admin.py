from django.contrib import admin
from django.contrib.auth.models import User
from .models import Journal, Entries, Goal, User, Timer

# Register your models here.
class JournalInline(admin.StackedInline):
    model = Journal

class EntryInline(admin.StackedInline):
    model = Entries

class GoalInline(admin.StackedInline):
    model = Goal

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [JournalInline, EntryInline, GoalInline]

admin.site.register(User, UserAdmin)
admin.site.register(Journal)
admin.site.register(Goal)
admin.site.register(Entries)
admin.site.register(Timer)
