from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class visitka(models.Model):
    name_page = models.CharField(verbose_name='Имя страницы', max_length=30, unique="True", blank="True")
    logo = models.ImageField(verbose_name='Логотип компании', upload_to='logo/')
    adress = models.TextField(verbose_name='Адрес')
    mobile_number = PhoneNumberField(verbose_name='Номер телефона', region='RU')
    email_adress = models.EmailField(verbose_name='Электронная почта', default="et@vvs-kaluga.ru")
    city_title = models.CharField(verbose_name='Город (Предложный.падеж)', max_length=30, blank="True", null="False")

    def __str__(self):
        return self.name_page

    class Meta:
        verbose_name = 'Визитка'
        verbose_name_plural = 'Визитки'