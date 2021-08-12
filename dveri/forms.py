from django import forms

TYPE_DOOR = [('Input', 'Входные'), ('InterRoom', 'Межкомнатные'), ]

TARGET_DOOR = [('Квартира', 'Квартира'), ('Частный дом', 'Частный дом'), ('Коттедж', 'Коттедж'), ('Офис', 'Офис'), ('Подъезд', 'Подъезд'), ]
FINISHING = [('Винилискожа', 'Винилискожа'), ('Ламинированная панель', 'Ламинированная панель'), ('Нитроэмаль', 'Нитроэмаль'), ]
DOP_INPUT = [('Нержавеющий порог', 'Нержавеющий порог'), ('Дверной отбойник', 'Дверной отбойник'), ('Декоративные откосы', 'Декоративные откосы'), ]

TYPE_INTERROOM = [('Распашная', 'Распашная'), ('Дверь-книжка', 'Дверь-книжка'), ('Дверь-пинал', 'Дверь-пинал'), ]
QUANITY_DOORS = [('1', '1'), ('2', '2'), ('3 и более', '3 и более'), ]
TYPE_PLATING = [('Натуральный шпон', 'Натуральный шпон'), ('Эмаль', 'Эмаль'), ('Эмаль по шпону', 'Эмаль по шпону'), ('Акрил', 'Акрил'), ]
DOP_INTERROOM = [('Наличники', 'Наличники'), ('Коробки', 'Коробки'), ('Моноблок для компланарной системы', 'Моноблок для компланарной системы'), ]


COMMUNICATION_METHOD = [('По телефону', 'Позвоните мне'), ('WhatsApp', 'Пришлите на WhatsApp'), ('SMS', 'Отправьте СМС'), ]


class CalcForm(forms.Form):

    type_door = forms.ChoiceField(
        label='Тип двери', widget=forms.RadioSelect, choices=TYPE_DOOR,)

    # Входные
    target_door = forms.ChoiceField(
        label='Назначение двери', widget=forms.RadioSelect, choices=TARGET_DOOR, required=False, )
    exterior_finish = forms.ChoiceField(
        label='Какая внешняя отделка наиболее привлекательна?', widget=forms.RadioSelect, choices=FINISHING, required=False, )
    interior_finish = forms.ChoiceField(
        label='Какая внутренняя отделка наиболее привлекательна?', widget=forms.RadioSelect, choices=FINISHING, required=False, )
    dop_input = forms.ChoiceField(
        label='Дополнительные комплектующие', widget=forms.CheckboxSelectMultiple, choices=DOP_INPUT, required=False, )
    # Межкомнатные
    type_InterRoom = forms.ChoiceField(
        label='Какую дверь вы хотите?', widget=forms.RadioSelect, choices=TYPE_INTERROOM, required=False,)
    quanity_doors = forms.ChoiceField(
        label='Количество дверей', widget=forms.RadioSelect, choices=QUANITY_DOORS, required=False,)
    type_plating = forms.ChoiceField(
        label='Какой тип покрытия наиболее привликателен?', widget=forms.RadioSelect, choices=TYPE_PLATING, required=False, )
    dop_InterRoom = forms.ChoiceField(
        label='Дополнительные комплектующие', widget=forms.CheckboxSelectMultiple, choices=DOP_INTERROOM, required=False, )

    communication_method = forms.ChoiceField(
        label='Как вы хотите узнать стоимость?', widget=forms.RadioSelect, choices=COMMUNICATION_METHOD, required=False, )
    number_phone = forms.CharField(label='Введите номер телефона')