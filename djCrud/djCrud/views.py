from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    context  = {
        'name':"login page"
    }
    return render(request, 'login.html', context)
