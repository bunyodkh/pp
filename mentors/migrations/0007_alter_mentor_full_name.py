# Generated by Django 5.1.6 on 2025-05-15 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0006_remove_mentor_show_on_website_mentor_show_on_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя и фамилия'),
        ),
    ]
