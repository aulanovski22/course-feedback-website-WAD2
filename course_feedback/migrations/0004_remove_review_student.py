# Generated by Django 2.2.28 on 2023-02-28 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_feedback', '0003_review_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='student',
        ),
    ]