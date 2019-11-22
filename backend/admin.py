# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Client, User, Location, Test_Standard, Product, Certificate, Test_Sequence, Performance_Data, Service

from django.contrib import admin

# Register your models here.
myModels = [Client, User, Location, Test_Standard, Product, Certificate, Test_Sequence, Performance_Data, Service]
admin.site.register(myModels)