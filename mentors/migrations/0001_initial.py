# Generated by Django 5.1.6 on 2025-04-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя и фамилия')),
                ('organization', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название организации')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('tg', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telegram')),
                ('linkedin_profile', models.CharField(blank=True, max_length=100, null=True, verbose_name='Linkedin')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Почему хотите стать ментором?')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mentors/', verbose_name='Фотография')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Наставник',
                'verbose_name_plural': 'Наставники',
            },
        ),
    ]
