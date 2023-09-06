from django.shortcuts import render
from time import strftime, gmtime


def current_date(request):
    context ={
        "date": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, template_name='date.html', context=context)

