# Generated by Django 5.1.6 on 2025-05-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_alter_participant_presentation_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='consent',
            field=models.CharField(choices=[('yes', 'Согласен'), ('no', 'Не согласен')], default='no', max_length=3, verbose_name='Согласны ли вы со съемкой вашей презентации, публикацией информации о вашем стартапе и делиться своими контактами с партнерами проекта и заинтересованными сторонами?'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='has_attracted_investment',
            field=models.CharField(choices=[('yes', 'Да'), ('no', 'Нет')], default='no', max_length=3, verbose_name='Привлекали ли вы инвестиции в свой стартап?'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='has_entrepreneurship_experience',
            field=models.CharField(choices=[('yes', 'Да'), ('no', 'Нет')], default='no', max_length=3, verbose_name='У вас был предпринимательский опыт ранее?'),
        ),
    ]
