# Generated by Django 3.2.7 on 2022-04-12 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_auto_20220412_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitionbadge',
            name='condition',
        ),
    ]