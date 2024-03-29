# Generated by Django 5.0.2 on 2024-02-14 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_number', models.IntegerField(unique=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_classes', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_class', models.CharField(max_length=50)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField(blank=True, null=True)),
                ('attended_date', models.DateField(auto_now_add=True)),
                ('attended_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_attendance', to='course.course_classes')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_attendance', to='course.student')),
            ],
        ),
    ]
