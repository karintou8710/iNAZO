# Generated by Django 3.1.7 on 2021-04-30 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeinfo',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='gradeinfo',
            name='created_at',
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False),
        ),
    ]
