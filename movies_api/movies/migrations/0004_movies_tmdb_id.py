# Generated by Django 3.0.7 on 2020-06-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200620_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='tmdb_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
