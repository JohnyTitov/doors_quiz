from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

TYPES = [
    ('classic', 'Классический'),
    ('modern', 'Современный'),
    ('loft', 'Лофт'),
    ('hi_tech', 'Хай тек'),
    ('another', 'Другой'), ]

COLORS = [
        ('white', 'Белый'),
        ('wood', 'Под дерево'),
        ('black', 'Чёрный'),
        ('fresh', 'Цветной'),
        ('another', 'Другой'), ]

FEEDBACK = [
    ('telegram', 'Telegram'),
    ('whatsapp', 'Whatsapp'),
    ('sms', 'Пришлите СМС'),
    ('phone', 'Позвоните мне'),
]


class PageShop(models.Model):
    name_page = models.CharField(verbose_name='Имя страницы', max_length=40, unique=True,)
    logo = models.ImageField(verbose_name='Логотип компании', upload_to='logo/', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес')
    phone = PhoneNumberField(verbose_name='Номер телефона', region='RU')
    email = models.EmailField(verbose_name='Электронная почта')
    city = models.CharField(verbose_name='Город (Предложный.падеж)', max_length=30)

    def __str__(self):
        return self.name_page

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class ClientChoice(models.Model):
    phone = PhoneNumberField(verbose_name='Номер телефона')
    type_door = models.CharField(verbose_name='Тип двери', max_length=50, choices=TYPES, default='another')
    color_door = models.CharField(verbose_name='Цвет', max_length=50, choices=COLORS, default='another')
    feedback = models.CharField(verbose_name='Обратная связь', max_length=50, choices=FEEDBACK, default='phone')

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
