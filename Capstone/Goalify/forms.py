from django import forms
from django.forms import ModelForm
from .models import Journal, Goal, Entries, Timer

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ('journal_style', 'journal_color', 'journal_name','user')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['journal_color'].label = "Color"
        self.fields['journal_name'].label = ""
        self.fields['journal_style'].widget.attrs['id'] = "journal_style"
        self.fields['journal_style'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['journal_color'].widget = forms.HiddenInput()
        self.fields['journal_color'].widget.attrs['id'] = "journal_color"
        self.fields['journal_name'].widget.attrs['placeholder'] = "Name Your Journal"
        self.fields['journal_name'].widget.attrs['id'] = "journal_name"

class EntryForm(ModelForm):
    class Meta:
        model = Entries
        fields = ('date','content', 'journal')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['journal'].widget = forms.HiddenInput()
        self.fields['content'].widget = forms.Textarea(attrs={'rows': 12, 'cols': 52, 'placeholder': "Write New Journal Entry"})
        self.fields['content'].widget.attrs['id'] = "entry_content"


class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ('name','goal_time', 'frequency', 'date', 'user', 'progress_start', 'progress_total')


    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['goal_time'].label = ""
        self.fields['frequency'].label = ""
        self.fields['date'].label = ""
        self.fields['name'].widget.attrs['placeholder'] = "Write a New Goal"
        self.fields['goal_time'].widget.attrs['placeholder'] = "Duration of Goal"
        self.fields['frequency'].widget.attrs['placeholder'] = "Number of Goal Attempts" 
        self.fields['name'].widget.attrs['id'] = "goals"
        self.fields['goal_time'].widget.attrs['id'] = "goals"
        self.fields['frequency'].widget.attrs['id'] = "goals"
        self.fields['date'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['progress_start'].widget = forms.HiddenInput()
        self.fields['progress_total'].widget = forms.HiddenInput()

class TimerForm(ModelForm):
    class Meta:
        model = Timer
        fields = ('id', 'time')
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()
        self.fields['time'].widget = forms.HiddenInput()

class ProgressForm(ModelForm):
    class Meta:
        model = Goal
        fields = ('progress_start',)
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['progress_start'].widget = forms.HiddenInput()
