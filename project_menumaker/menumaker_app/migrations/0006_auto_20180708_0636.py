# Generated by Django 2.0.6 on 2018-07-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menumaker_app', '0005_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.URLField(default='https://pixabay.com/photo-575434/', max_length=300),
        ),
    ]
