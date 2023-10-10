from django import forms
from .models import DateConversion


class ConversionTypeForm(forms.ModelForm):
    class Meta:
        model = DateConversion
        fields = ['conversion_type']


class DateConversionPersianForm(forms.ModelForm):
    class Meta:
        model = DateConversion
        fields = ['year', 'persian_month', 'day']


class DateConversionInternationalForm(forms.ModelForm):
    class Meta:
        model = DateConversion
        fields = ['year', 'international_month', 'day']

