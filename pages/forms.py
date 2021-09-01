from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import ClientChoice
from django.core.validators import RegexValidator

validate_numeric = RegexValidator(r'^[0-9]*$', 'ввод только цифр!')


class SelectForm(ModelForm):
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

    type_door = forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect, required=False, )
    color_door = forms.ChoiceField(choices=COLORS, widget=forms.RadioSelect, required=False, )
    feedback = forms.ChoiceField(choices=FEEDBACK, widget=forms.RadioSelect, required=False, )
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='RU',
                             attrs={'placeholder ': '(999)-999-99-99',
                                    'maxlength': '10',
                                    'class': 'phone-field',
                                    'pattern': '^[ 0-9]+$', },
                             ))

    class Meta:
        model = ClientChoice
        fields = ['phone', ]
