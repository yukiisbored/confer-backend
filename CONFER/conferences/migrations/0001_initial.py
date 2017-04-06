# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('source_url', models.CharField(blank=True, max_length=512, null=True)),
                ('website', models.CharField(blank=True, max_length=512, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('cfp_closes', models.DateTimeField(blank=True, null=True)),
                ('finaid_closes', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('place', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('postcode', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('geo_lat', models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True, verbose_name='latitude')),
                ('geo_long', models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True, verbose_name='longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='conference',
            name='tags',
            field=models.ManyToManyField(blank=True, to='conferences.Tag'),
        ),
    ]
