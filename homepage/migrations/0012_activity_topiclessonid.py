# Generated by Django 3.2.7 on 2022-04-08 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20220323_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='topiclessonid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.topiclesson'),
        ),
    ]