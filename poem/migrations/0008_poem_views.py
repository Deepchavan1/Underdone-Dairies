# Generated by Django 3.2.6 on 2021-11-26 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0007_remove_poem_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
