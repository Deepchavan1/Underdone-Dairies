# Generated by Django 3.2.6 on 2021-11-23 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0002_alter_poem_thumbnail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poem',
        ),
    ]
