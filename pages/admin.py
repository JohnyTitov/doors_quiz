from django.contrib import admin
from .models import PageShop, ClientChoice


class AdminPageShop(admin.ModelAdmin):
    list_display = ('name_page', 'address', 'phone', 'email', 'city', 'logo')
    list_display_links = ('name_page', 'address')
    search_fields = ('name_page', 'address', 'phone')


class AdminClientChoice(admin.ModelAdmin):
    list_display = ('shop', 'phone', 'feedback', 'type_door', 'color_door')
    list_display_links = ('shop', 'phone', 'feedback', 'type_door', 'color_door')
    search_fields = ('shop', 'phone', 'feedback', 'type_door', 'color_door')
    list_filter = ('shop', 'feedback', 'type_door', 'color_door')


admin.site.register(PageShop, AdminPageShop)
admin.site.register(ClientChoice, AdminClientChoice)
