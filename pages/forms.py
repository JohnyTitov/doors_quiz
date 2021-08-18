from django import forms


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

    type_door = forms.ChoiceField(choices=TYPES, widget=forms.RadioSelect, )
    color_door = forms.ChoiceField(choices=COLORS, widget=forms.RadioSelect, )
