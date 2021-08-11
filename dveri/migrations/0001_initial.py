# Generated by Django 3.1.4 on 2021-01-20 12:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visitka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_page', models.CharField(max_length=30, verbose_name='Имя страницы')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип компании')),
                ('adress', models.TextField(verbose_name='Адрес')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Визитка',
                'verbose_name_plural': 'Визитки',
            },
        ),
    ]