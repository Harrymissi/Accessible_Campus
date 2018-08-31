# Generated by Django 2.0.3 on 2018-07-29 23:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstgis', '0008_auto_20180727_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessble_Entr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Accessble Entrance',
            },
        ),
        migrations.CreateModel(
            name='Handi_Transit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Handi Transit Stop',
            },
        ),
    ]
