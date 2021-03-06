# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('floor', models.CharField(max_length=200)),
                ('has_podium', models.BooleanField()),
                ('commissioned_date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
