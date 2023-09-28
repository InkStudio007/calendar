from django import forms
from django_jalali import forms as jforms
from .models import DateConversion


class DateConversionForm(forms.ModelForm):
    class Meta:
        model = DateConversion
        fields = '__all__'

