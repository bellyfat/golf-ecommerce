from django.shortcuts import render, redirect, reverse
from django.template.context_processors import csrf
from forms import teeTimeForm
from django.conf import settings



def get_teeTime(request):
    return render(request, "teetime.html")

def requested_teeTime(request):
    form = teeTimeForm(request.POST)
    if request.method == 'POST':
        return render(request, "teetimeMessage.html")

    else:
        print ('Please call the Golf Shop')

