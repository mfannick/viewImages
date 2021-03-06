# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagesUpload/')),
                ('imageName', models.CharField(max_length=30)),
                ('imageDescription', models.TextField()),
                ('imageUrl', models.URLField()),
                ('postedTime', models.DateTimeField(auto_now_add=True)),
                ('categoryF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Category')),
                ('editorF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Editor')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='locationF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Location'),
        ),
    ]
