# Generated by Django 5.1.6 on 2025-04-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0005_mentor_registration_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='show_on_website',
        ),
        migrations.AddField(
            model_name='mentor',
            name='show_on_main',
            field=models.BooleanField(default=False, verbose_name='Показать на главной странице'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='show_on_page',
            field=models.BooleanField(default=False, verbose_name='Показать на странице менторов'),
        ),
    ]
