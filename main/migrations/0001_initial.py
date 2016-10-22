# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-22 21:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('prereq', models.CharField(max_length=128)),
                ('credits', models.IntegerField()),
                ('fall', models.BooleanField()),
                ('winter', models.BooleanField()),
                ('spring', models.BooleanField()),
                ('summer', models.BooleanField()),
                ('dormant', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DegreeRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required', models.BooleanField()),
                ('phase', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('reqcredits', models.IntegerField()),
                ('online', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditCnt', models.IntegerField(default=0)),
                ('isEnrolled', models.BooleanField()),
                ('isFaculty', models.BooleanField()),
                ('degree', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Degrees')),
                ('usr_acct', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='degreerequirements',
            name='degree_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Degrees'),
        ),
        migrations.AddField(
            model_name='completedclasses',
            name='courseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Courses'),
        ),
        migrations.AddField(
            model_name='completedclasses',
            name='studentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Users'),
        ),
    ]
