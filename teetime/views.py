from django.shortcuts import render, redirect, reverse
from django.template.context_processors import csrf
from forms import teeTimeForm
from django.conf import settings
from products.models import Product


def get_teeTime(request):
    return render(request, "teetime.html")

def requested_teeTime(request):
    return render(request, "teetimeMessage.html")



