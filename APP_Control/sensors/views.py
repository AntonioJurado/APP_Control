# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import  HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Sensor, Terreno

def index(request):
	#import ipdb; ipdb.set_trace()

	sensors= Sensor.objects.all()

	return render(request,'sensors/index.html',
		{'sensors': sensors}
		)

#en esta vista mandaremos los POST para luego tratar los datos
def data(request):

	return HttpResponse("aqui cojo los datos")


def results(request, sensor_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def detail(request, question_id):
	return HttpResponse("You're looking the details.")