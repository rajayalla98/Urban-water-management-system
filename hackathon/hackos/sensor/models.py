from __future__ import unicode_literals
from django.db import models

class sensor(models.Model):
	#tem_value=models.CharField(max_length=250)
	#hum_value=models.CharField(max_length=250)
	soil_value=models.CharField(max_length=250)
	water_level=models.CharField(max_length=250)
	water_flow=models.CharField(max_length=250)
	turbidity=models.CharField(max_length=250)
	ph=models.CharField(max_length=250)
	result=models.CharField(max_length=1000)