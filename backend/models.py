# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=20)
    client_type = models.CharField(max_length=20)
    @property
    def client_id(self):
        return self.id


class User(models.Model):
    username = models.CharField(max_length=20, default='')
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    ophone = models.CharField(max_length=20)
    cphone = models.CharField(max_length=20)
    prefix = models.CharField(max_length=20)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)


class Location(models.Model):
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)


class Test_Standard(models.Model):
    standard_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    published_date = models.CharField(max_length=20)


class Product(models.Model):
    product_name = models.CharField(max_length=20)
    cell_technology = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    number_of_cells = models.CharField(max_length=20)
    number_of_cells_in_series = models.CharField(max_length=20)
    number_of_series_strings = models.CharField(max_length=20)
    number_of_diodes = models.CharField(max_length=20)
    product_length = models.CharField(max_length=20)
    product_width = models.CharField(max_length=20)
    product_weight = models.CharField(max_length=20)
    superstate_type = models.CharField(max_length=20)
    superstate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    substrate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.CharField(max_length=20)
    encapsulation_type = models.CharField(max_length=20)
    encapsulation_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)


class Certificate(models.Model):
    certificate_ID = models.CharField(max_length=20)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.CharField(max_length=20)
    issue_date = models.CharField(max_length=20)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
    location_ID = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)


class Test_Sequence(models.Model):
    sequence_name = models.CharField(max_length=20)


class Performance_Data(models.Model):
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_ID = models.ForeignKey(Test_Sequence, on_delete=models.CASCADE)
    max_system_volage = models.CharField(max_length=20)
    voc = models.CharField(max_length=20)
    lsc = models.CharField(max_length=20)
    vmp = models.CharField(max_length=20)
    imp = models.CharField(max_length=20)
    pmp = models.CharField(max_length=20)
    ff = models.CharField(max_length=20)


class Service(models.Model):
    service_name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    is_FI_required = models.CharField(max_length=20)
    FI_frequency = models.CharField(max_length=20)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
