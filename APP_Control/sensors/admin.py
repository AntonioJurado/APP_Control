# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

from .models import Sensor, Terreno

# Register your models here.

admin.site.register(Sensor)
admin.site.register(Terreno)