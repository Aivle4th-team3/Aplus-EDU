from django import forms
from .models import Calendar


class CalendarModelForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['author', 'title', 'label', 'startdate', 'enddate']
