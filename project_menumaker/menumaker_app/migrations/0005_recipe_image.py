# Generated by Django 2.0.6 on 2018-07-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menumaker_app', '0004_auto_20180708_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipe_images'),
        ),
    ]