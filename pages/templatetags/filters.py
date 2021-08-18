from django import template

register = template.Library()


# Преобразование телефонного номера
@register.filter(name='phone_filter')
def phone_filter(arg):
    if len(arg) == 0:
        arg = "+78005553535"    # Default number
    result = arg[0:2] + ' (' + arg[2:5] + ') ' + arg[5:8] + '-' + arg[8:10] + '-' + arg[10:12]
    return result


@register.filter(name='module_2')
def module_2(arg):
    return arg % 2 == 0
