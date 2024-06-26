# Generated by Django 3.0.7 on 2022-03-23 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_owncompetitionbadge_ownlessonbadge'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingTimeTest',
            fields=[
                ('trackingtimetestid', models.AutoField(primary_key=True, serialize=False)),
                ('max_wpm', models.IntegerField(blank=True, null=True)),
                ('max_cpm', models.IntegerField(blank=True, null=True)),
                ('createdate', models.DateField(auto_now_add=True, null=True)),
                ('editdate', models.DateTimeField(auto_now=True, null=True)),
                ('isenable', models.BooleanField(blank=True, default=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('accountid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Account')),
                ('timetestid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Competition')),
            ],
            options={
                'db_table': 'TrackingTimeTest',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TrackingContentTest',
            fields=[
                ('trackingcontenttestid', models.AutoField(primary_key=True, serialize=False)),
                ('max_wpm', models.IntegerField(blank=True, null=True)),
                ('max_cpm', models.IntegerField(blank=True, null=True)),
                ('createdate', models.DateField(auto_now_add=True, null=True)),
                ('editdate', models.DateTimeField(auto_now=True, null=True)),
                ('isenable', models.BooleanField(blank=True, default=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('accountid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Account')),
                ('timetestid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.Competition')),
            ],
            options={
                'db_table': 'TrackingContentTest',
                'managed': True,
            },
        ),
    ]
