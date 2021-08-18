from django import forms


class SelectForm(forms.Form):
    TYPE_DOOR = [
        ('classic', 'Классический'),
        ('modern', 'Современный'),
        ('loft', 'Лофт'),
        ('hi_tech', 'Хай тек'),
        ('another', 'Другой'), ]

    type_door = forms.ChoiceField(choices=TYPE_DOOR, widget=forms.RadioSelect, )
