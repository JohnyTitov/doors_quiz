# Generated by Django 3.2.6 on 2021-09-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_clientchoice_color_door'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientchoice',
            name='feedback',
            field=models.CharField(blank=True, choices=[('telegram', 'Telegram'), ('whatsapp', 'Whatsapp'), ('sms', 'Пришлите СМС'), ('phone', 'Позвоните мне')], max_length=50, null=True, verbose_name='Обратная связь'),
        ),
    ]
