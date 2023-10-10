from django.shortcuts import render
from .forms import *
from DateConvert import converter

# Create your views here.


def date_conversion(request):
    return render(request, 'date_conversion.html')


def date_conversion_international(request):
    form_international = DateConversionInternationalForm(request.POST)

    if form_international.is_valid():
        year = form_international.cleaned_data['year']
        international_month = form_international.cleaned_data['international_month']
        day = form_international.cleaned_data['day']

        international_to_persian = converter.gregorian_to_jalali(year, international_month, day)

        international_to_persian = f"{international_to_persian[0]}/{international_to_persian[1]}/{international_to_persian[2]}"

        form_international.save()

        return render(request, 'date_conversion_international.html', {
            'international_to_persian': international_to_persian
        })

    return render(request, 'date_conversion_international.html', {
        'form_international': form_international
    })


def date_conversion_persian(request):
    form_persian = DateConversionPersianForm(request.POST)

    if form_persian.is_valid():
        year = form_persian.cleaned_data['year']
        persian_month = form_persian.cleaned_data['persian_month']
        day = form_persian.cleaned_data['day']

        persian_to_international = converter.jalali_to_gregorian(year, persian_month, day)

        persian_to_international = f"{persian_to_international[0]}/{persian_to_international[1]}/{persian_to_international[2]}"

        form_persian.save()

        return render(request, 'date_conversion_persian.html', {
            'persian_to_international': persian_to_international
        })

    return render(request, 'date_conversion_persian.html', {
        'form_persian': form_persian,
    })
