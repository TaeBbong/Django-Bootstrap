# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-07 14:07
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='thumb'),
        ),
    ]
