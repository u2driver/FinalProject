import re
from django.utils.timezone import datetime
from django.http import HttpResponse
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