from django import forms
from .models import DateConversion


class DateConversionForm(forms.ModelForm):
    class Meta:
        model = DateConversion
        fields = '__all__'

