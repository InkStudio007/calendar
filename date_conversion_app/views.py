from django.shortcuts import render
from .forms import DateConversionForm
from datetime import date, timedelta
from DateConvert import converter

# Create your views here.


def date_conversion(request):
    form = DateConversionForm(request.POST)
    if form.is_valid():
        conversion_type = form.cleaned_data['conversion_type']
        international_month = form.cleaned_data['international_month']
        persian_month = form.cleaned_data['persian_month']
        year = form.cleaned_data['year']
        day = form.cleaned_data['day']

        international_to_persian = converter.gregorian_to_jalali(year, international_month, day)
        persian_to_international = converter.jalali_to_gregorian(year, persian_month, day)

        form.save()

        return render(request, 'date_conversion.html', {
            'conversion_type': conversion_type,
            'persian_to_international': persian_to_international,
            'international_to_persian': international_to_persian,
        })
    return render(request, 'date_conversion.html', {
        'form': form,
    })
