# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-05-31 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STC_pro_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_assignment',
            name='ans_img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]