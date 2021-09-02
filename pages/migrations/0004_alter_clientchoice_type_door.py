# Generated by Django 3.2.6 on 2021-09-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210901_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientchoice',
            name='type_door',
            field=models.CharField(blank=True, choices=[('classic', 'Классический'), ('modern', 'Современный'), ('loft', 'Лофт'), ('hi_tech', 'Хай тек'), ('another', 'Другой')], default='another', max_length=50, verbose_name='Тип двери'),
        ),
    ]