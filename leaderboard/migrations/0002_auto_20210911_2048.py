# Generated by Django 3.2.7 on 2021-09-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='event11',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='event12',
            field=models.IntegerField(default=0),
        ),
    ]
