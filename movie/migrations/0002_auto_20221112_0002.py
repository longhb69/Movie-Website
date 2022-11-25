# Generated by Django 3.2.13 on 2022-11-11 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch', to='movie.movie'),
            preserve_default=False,
        ),
    ]