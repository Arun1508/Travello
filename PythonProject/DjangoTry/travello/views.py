from django.shortcuts import render
from .models import Destination
from .fileRead import fileOperation


def home(request):

    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest});
