from django.shortcuts import render
from .forms import DateDifferenceForm

# Create your views here.
def date_difference(request):
    form = DateDifferenceForm()
    if request.method == 'POST':
        form = DateDifferenceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_date = data['from_date']
            end_date = data['to_date']
            form.save()

    return render(request, "date_difference.html", {'form': form, 'start_date': start_date, 'end_date': end_date})


