# Generated by Django 3.2.7 on 2022-03-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_topiclesson_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='lessonbadge',
            name='condition',
        ),
        migrations.DeleteModel(
            name='LessonInstruction',
        ),
    ]
