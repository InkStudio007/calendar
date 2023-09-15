from django import forms
from .models import AgeCalculator


class AgeCalculatorForm(forms.ModelForm):
    class Meta:
        model = AgeCalculator
        fields = '__all__'
        widgets = {'birthday_date': forms.DateInput(format=('%Y/%m/%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'})}

