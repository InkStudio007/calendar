from django import forms
from .models import DateDifference


class DateDifferenceForm(forms.ModelForm):
    class Meta:
        model = DateDifference
        fields = ['from_date', 'to_date']
        widgets = {'from_date': forms.DateInput(format=("%Y/%m/%d"), attrs={'class': 'form-control','placeholder':'select a date', 'type':'date'}),

        'to_date': forms.DateInput(format=("%Y/%M/%d"), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
