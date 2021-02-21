from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404


def login(request):
    context  = {
        'name':"login page"
    }
    return render(request, 'login.html', context)
