# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import items.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', items.fields.ThumbnailImageField(upload_to=b'photos')),
                ('caption', models.CharField(max_length=250, blank=True)),
                ('votes', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='items.Item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
