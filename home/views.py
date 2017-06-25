from django.shortcuts import render

from django.template.context_processors import csrf

# I will create my views here

def get_index(request):
    args = {}
    args
    return render(request, "index.html")


def handle_message_form(request):
    return render(request, "message.html")


def loginMembers(request):
    return render(request, "login.html")
