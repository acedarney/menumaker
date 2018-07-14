# Generated by Django 2.0.6 on 2018-07-14 12:40

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menumaker_app', '0009_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=[{'name': '', 'prepared': '', 'qty': ''}], size=None),
        ),
    ]
