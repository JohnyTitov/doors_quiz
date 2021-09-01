from django.contrib import admin
from .models import PageShop, ClientChoice


class AdminPageShop(admin.ModelAdmin):
    list_display = ('name_page', 'address', 'phone', 'email', 'city', 'logo')
    list_display_links = ('name_page', 'address')
    search_fields = ('name_page', 'address', 'phone')


class AdminClientChoice(admin.ModelAdmin):
    list_display = ('phone',)
    list_display_links = ('phone',)
    search_fields = ('phone',)


admin.site.register(PageShop, AdminPageShop)
admin.site.register(ClientChoice, AdminClientChoice)
