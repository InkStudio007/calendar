from django.shortcuts import render
from .forms import DateDifferenceForm
from datetime import datetime


def date_difference(request):
    form = DateDifferenceForm(request.POST)
    if form.is_valid():
        start_date = form.cleaned_data['from_date']
        end_date = form.cleaned_data['to_date']
        total = (end_date-start_date)

        form.save()
        return render(request, 'date_difference.html', {'form': form, 'total': total})
    return render(request, 'date_difference.html', {'form': form})


