from django.contrib import admin
from .models import PageShop


class AdminPageShop(admin.ModelAdmin):
    list_display = ('name_page', 'address', 'phone', 'email', 'city', 'logo')
    list_display_links = ('name_page', 'address')
    search_fields = ('name_page', 'address', 'phone')


admin.site.register(PageShop, AdminPageShop)
