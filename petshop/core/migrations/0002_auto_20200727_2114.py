# Generated by Django 3.0.8 on 2020-07-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='idade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pet',
            name='nome',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]