from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import ClientChoice
from django.core.validators import RegexValidator

validate_numeric = RegexValidator(r'^[0-9]*$', 'ввод только цифр!')


class SelectForm(ModelForm):
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='RU',
                             attrs={'placeholder ': '(999)-999-99-99',
                                    'maxlength': '10',
                                    'class': 'phone-field',
                                    'pattern': '^[ 0-9]+$', },
                             ))

    class Meta:
        model = ClientChoice
        fields = ['shop', 'phone', 'type_door', 'color_door', 'feedback']
        widgets = {'type_door': forms.RadioSelect(),
                   'color_door': forms.RadioSelect(),
                   'feedback': forms.RadioSelect(), }
