from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class SelectForm(forms.Form):
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

    type_door = forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect, )
    color_door = forms.ChoiceField(choices=COLORS, widget=forms.RadioSelect, )
    feedback = forms.ChoiceField(choices=FEEDBACK, widget=forms.RadioSelect, )
    #phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+7(999) 999 99-99'}), )
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(), )
