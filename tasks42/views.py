from django.shortcuts import render
from tasks42.models import Person


def index(request):
    context = {'persons': Person.objects.all()[0]}
    return render(request, "home.html", context)
