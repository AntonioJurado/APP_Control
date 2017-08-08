# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User #lib para importar usuario

# Create your models here.

#El usuario lo heredamos de la clase user de django

class Terreno(models.Model):

	user_terreno = models.ForeignKey('auth.User')
	pos_terreno_lat = models.DecimalField(max_digits=10, decimal_places=6)
	pos_terreno_long = models.DecimalField(max_digits=10, decimal_places=6)


	#sensorZona = models.ForeignKey('Terreno', blank=True, null=True, related_name='contiene') #Sensor utilizado por

	"""docstring for Terreno"""
#	def __unicode__(self): #muestra por defecto
#		return self.user_terreno
		

class Sensor(models.Model):

	sensor_device = models.CharField(max_length = 5) #Sensor master de la finca
	id_subsensor = models.IntegerField(max_length = 3) #id de subsensor del master
	sensor_datatime	= models.DateTimeField(auto_now=True) #fecha del mensaje
	temp_master = models.CharField(max_length = 255, null=True) #vector con la temperatura

	zona = models.ForeignKey('Sensor', blank=True, null=True, related_name='sensores') #Sensores con los que cuenta

	"""docstring for Sensor"""
#	def __unicode__(self): #muestra por defecto
#		return self.sensor_device
		