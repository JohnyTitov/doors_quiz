from django.contrib import admin
from .models import visitka


class AdminVisit(admin.ModelAdmin):
    list_display = ('name_page', 'adress', 'mobile_number', 'email_adress', 'city_title', 'logo')
    list_display_links = ('name_page', 'adress')
    search_fields = ('name_page', 'adress', 'mobile_number')


admin.site.register(visitka, AdminVisit)
