from django import template

register = template.Library()


# Преобразование телефонного номера
@register.filter(name='phone_filter')
def phone_filter(arg):
    result = arg[0:2] + ' (' + arg[2:5] + ') ' + arg[5:8] + '-' + arg[8:10] + '-' + arg[10:12]
    return result
