import tkinter

from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from time import *
from tkinter import *
import json


def main_calendar(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    main_cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'calendar.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'main_cal': main_cal,
    })


def current_calendar(request):
    now = datetime.now()
    current_date = now.strftime("%Y-%b-%d %A")

    current_cal = HTMLCalendar().formatmonth(now.year, now.month)

    string_clock = now.strftime("%H:%M:%S %p")

    return render(request, 'home.html', {
        'current_date': current_date,
        'current_cal': current_cal,
        'clock': string_clock,
    })






