# Generated by Django 3.2.6 on 2022-11-22 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='score',
        ),
    ]
