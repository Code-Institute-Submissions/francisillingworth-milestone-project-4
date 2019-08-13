# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-13 17:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='features_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
