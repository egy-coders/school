# Generated by Django 5.2.4 on 2025-07-23 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentcourse',
            options={'verbose_name': 'Enrollement'},
        ),
        migrations.AlterUniqueTogether(
            name='studentcourse',
            unique_together={('student', 'course')},
        ),
    ]
