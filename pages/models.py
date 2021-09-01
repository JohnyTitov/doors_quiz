from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
