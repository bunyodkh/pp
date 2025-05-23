# Generated by Django 5.1.6 on 2025-04-24 08:24

import core.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_alter_achievement_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventWinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название стартапа')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание стартапа')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=core.utils.rename_uploaded_image, verbose_name='Логотип стартапа')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_winners', to='events.event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Победитель',
                'verbose_name_plural': 'Победители',
                'ordering': ['-created_at'],
            },
        ),
    ]
