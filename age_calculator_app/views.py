from django.shortcuts import render
from .forms import AgeCalculatorForm
from datetime import date, datetime
import math

# Create your views here.


def age_calculator(request):
    form = AgeCalculatorForm(request.POST)
    today = date.today()

    if form.is_valid():
        birthday = form.cleaned_data['birthday_date']

        age = (today-birthday)
        age_days = age.days
        age_month = math.floor(age_days / 30)
        age_year = math.floor(age_month/12)
        age_year_days = age_year*365
        left_over_days_of_years = age_days-age_year_days
        left_over_months = math.floor(left_over_days_of_years/30)
        age_month_days = left_over_months*30
        left_over_days_of_months = left_over_days_of_years-age_month_days

        form.save()

        return render(request, 'age_calculator.html', {'form': form, 'year':age_year, 'month': left_over_days_of_months, 'day': left_over_days_of_months })
    return render(request, 'age_calculator.html', {'form': form})

