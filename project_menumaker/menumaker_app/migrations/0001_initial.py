# Generated by Django 2.0.6 on 2018-07-05 01:53

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
from django.contrib.postgres.operations import HStoreExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instructions', models.TextField()),
                ('ingredients', django.contrib.postgres.fields.hstore.HStoreField()),
                ('cuisine', models.CharField(max_length=30)),
                ('likes', django.contrib.postgres.fields.hstore.HStoreField()),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='recipes',
            field=models.ManyToManyField(to='menumaker_app.Recipe'),
        ),
    ]
