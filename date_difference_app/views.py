from django.shortcuts import render
from .forms import DateDifferenceForm
import math


def date_difference(request):
    form = DateDifferenceForm(request.POST)
    if form.is_valid():
        start_date = form.cleaned_data['from_date']
        end_date = form.cleaned_data['to_date']

        total = (end_date-start_date)

        age_days = total.days
        age_month = age_days.floor(age_days / 30)
        age_year = math.floor(age_month / 12)
        age_year_days = age_year * 365
        left_over_days_of_years = age_days - age_year_days
        left_over_months = math.floor(left_over_days_of_years / 30)
        age_month_days = left_over_months * 30
        left_over_days_of_months = left_over_days_of_years - age_month_days

        form.save()
        return render(request, 'date_difference.html', {'form': form, 'year': age_year, 'month': left_over_months, 'day': left_over_days_of_months, 'age_days': age_days})
    return render(request, 'date_difference.html', {'form': form})


