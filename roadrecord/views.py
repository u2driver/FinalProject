import re
from django.utils.timezone import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from .models import Accidents

def home(request):
  crashes = Accidents.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'crashes': crashes,
  }
  return HttpResponse(template.render(context, request))

def hello_there(request, name):
    return render(
        request,
        'roadrecord/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  v = request.POST['highway']
  w = request.POST['month']
  x = request.POST['day_night']
  y = request.POST['marker']
  z = request.POST['fatal_non']
  crash = Accidents(highway = v, month = w, day_night = x, marker = y, fatal_non = z)
  crash.save()
  return HttpResponseRedirect(reverse('home'))

def update(request, id):
  crashes = Accidents.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'crashes': crashes,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  highway = request.POST['highway']
  month = request.POST['month']
  day_night = request.POST['day_night']
  marker = request.POST['marker']
  fatal_non = request.POST['fatal_non']
  crashes = Accidents.objects.get(id=id)
  crashes.highway = highway
  crashes.month = month
  crashes.day_night = day_night
  crashes.marker = marker
  crashes.fatal_non = fatal_non
  crashes.save()
  return HttpResponseRedirect(reverse('home'))

def testing(request):
  crashes = Accidents.objects.filter(highway='I25', month = 'Jan', marker__range = (50, 60)).values()
  template = loader.get_template('template.html')
  context = {
    'crashes': crashes,
  }
  return HttpResponse(template.render(context, request))
