# Generated by Django 3.2.6 on 2021-09-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_clientchoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientchoice',
            name='color_door',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='clientchoice',
            name='feedback',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Обратная связь'),
        ),
        migrations.AddField(
            model_name='clientchoice',
            name='type_door',
            field=models.CharField(blank=True, choices=[('classic', 'Классический'), ('modern', 'Современный'), ('loft', 'Лофт'), ('hi_tech', 'Хай тек'), ('another', 'Другой')], max_length=50, null=True, verbose_name='Тип двери'),
        ),
    ]
