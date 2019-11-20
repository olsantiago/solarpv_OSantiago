# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_ID', models.CharField(max_length=20)),
                ('report_number', models.CharField(max_length=20)),
                ('issue_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=20)),
                ('client_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax_number', models.CharField(max_length=20)),
                ('client_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Performance_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_system_volage', models.CharField(max_length=20)),
                ('voc', models.CharField(max_length=20)),
                ('lsc', models.CharField(max_length=20)),
                ('vmp', models.CharField(max_length=20)),
                ('imp', models.CharField(max_length=20)),
                ('pmp', models.CharField(max_length=20)),
                ('ff', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('cell_technology', models.CharField(max_length=20)),
                ('cell_manufacturer', models.CharField(max_length=20)),
                ('number_of_cells', models.CharField(max_length=20)),
                ('number_of_cells_in_series', models.CharField(max_length=20)),
                ('number_of_series_strings', models.CharField(max_length=20)),
                ('number_of_diodes', models.CharField(max_length=20)),
                ('product_lenght', models.CharField(max_length=20)),
                ('product_width', models.CharField(max_length=20)),
                ('product_weight', models.CharField(max_length=20)),
                ('superstate_type', models.CharField(max_length=20)),
                ('superstate_manufacturer', models.CharField(max_length=20)),
                ('substrate_type', models.CharField(max_length=20)),
                ('substrate_manufacturer', models.CharField(max_length=20)),
                ('frame_type', models.CharField(max_length=20)),
                ('frame_adhesive', models.CharField(max_length=20)),
                ('encapsulation_type', models.CharField(max_length=20)),
                ('encapsulation_manufacturer', models.CharField(max_length=20)),
                ('junction_box_type', models.CharField(max_length=20)),
                ('junction_box_manufacturer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('is_FI_required', models.CharField(max_length=20)),
                ('FI_frequency', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('published_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('ophone', models.CharField(max_length=20)),
                ('cphone', models.CharField(max_length=20)),
                ('prefix', models.CharField(max_length=20)),
                ('client_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Client')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='standard_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Test_Standard'),
        ),
        migrations.AddField(
            model_name='performance_data',
            name='model_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product'),
        ),
        migrations.AddField(
            model_name='performance_data',
            name='sequence_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Test_Sequence'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='location_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Location'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='model_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='standard_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Test_Standard'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.User'),
        ),
    ]
