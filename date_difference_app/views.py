from django.shortcuts import render
from .forms import DateDifferenceForm
from math import floor

def date_difference(request):
    form = DateDifferenceForm(request.POST)
    if form.is_valid():
        start_date = form.cleaned_data['from_date']
        end_date = form.cleaned_data['to_date']

        total = (end_date-start_date)

        date_days = total.days
        date_month = floor(date_days / 30)
        date_year = floor(date_month / 12)
        date_year_days = date_year * 365
        left_over_days_of_years = date_days - date_year_days
        left_over_months = floor(left_over_days_of_years / 30)
        date_month_days = left_over_months * 30
        left_over_days_of_months = left_over_days_of_years - date_month_days

        form.save()

        return render(request, 'date_difference.html', {'form': form, 'year': date_year, 'month': left_over_months, 'day': left_over_days_of_months, 'date_days': date_days})
    return render(request, 'date_difference.html', {'form': form})


