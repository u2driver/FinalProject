from django.db import models

class Accidents(models.Model):
  highway = models.CharField(max_length=10)
  month = models.CharField(max_length=10)
  day_night = models.CharField(max_length=10)
  marker = models.IntegerField()
  fatal_non = models.CharField(max_length=10)
  