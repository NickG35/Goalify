from django import forms
from django.forms import ModelForm
from .models import Journal, Goal, Entries

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ('journal_style', 'journal_color', 'journal_name','user')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['journal_style'].label = ""
        self.fields['journal_color'].label = "Choose Color"
        self.fields['journal_name'].label = ""
        self.fields['user'].label = ""
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['journal_style'].widget.attrs['placeholder'] = "Pick Journal Color"
        self.fields['journal_style'].widget.attrs['placeholder'] = "Pick Journal Color"
        self.fields['journal_name'].widget.attrs['placeholder'] = "Name Your Journal"

class EntryForm(ModelForm):
    class Meta:
        model = Entries
        fields = ('date','content')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['date'].label = ""
        self.fields['content'].label = ""
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['content'].widget.attrs['placeholder'] = "Write New Journal Entry"



class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ('name','goal_time', 'frequency', 'date', 'progress')


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['goal_time'].label = ""
        self.fields['frequency'].label = ""
        self.fields['date'].label = ""
        self.fields['progress'].label = ""
        self.fields['name'].widget.attrs['placeholder'] = "Write a New Goal"
        self.fields['goal_time'].widget.attrs['placeholder'] = "Duration of Each Goal Attempt"
        self.fields['frequency'].widget.attrs['placeholder'] = "Number of Total Goal Attempts" 
