# Generated by Django 5.2.1 on 2025-06-03 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0006_course_teacher_address2_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address2',
            name='added',
        ),
        migrations.RemoveField(
            model_name='students',
            name='description',
        ),
    ]
