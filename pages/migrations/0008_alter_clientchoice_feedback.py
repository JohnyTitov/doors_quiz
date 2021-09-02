# Generated by Django 3.2.6 on 2021-09-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_clientchoice_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientchoice',
            name='feedback',
            field=models.CharField(choices=[('telegram', 'Telegram'), ('whatsapp', 'Whatsapp'), ('sms', 'Пришлите СМС'), ('phone', 'Позвоните мне')], default='phone', max_length=50, verbose_name='Обратная связь'),
        ),
    ]