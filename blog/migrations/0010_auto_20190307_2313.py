# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-07 14:13
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190307_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='devkor_logo_mini.png', upload_to='thumb'),
        ),
    ]
