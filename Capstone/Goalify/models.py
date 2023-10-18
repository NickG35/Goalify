from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Journal(models.Model):
    journal_style = models.ImageField(null=True, blank=True)
    journal_color = models.CharField(max_length = 15, null = True, blank = True)
    journal_name = models.CharField(max_length = 50, null = True, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.journal_name

class Entries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null = True, blank = True)
    date = models.DateTimeField(null = True, blank = True)
    content = models.CharField(max_length = 1000, null = True, blank = True)

    def __str__(self):
        return self.content

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 50, null = True, blank = True)
    goal_time = models.IntegerField(blank= True, null = True)
    frequency = models.IntegerField(blank = True, null = True)
    date = models.DateTimeField(null = True, blank = True)
    progress = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name