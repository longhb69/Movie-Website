# Generated by Django 3.2.13 on 2022-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_movie_flim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='flim',
            field=models.FileField(blank=True, upload_to='movies'),
        ),
    ]
