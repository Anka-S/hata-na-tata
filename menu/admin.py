from django.contrib import admin
from .models import MenuSection, MenuItem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MenuSection)

# Register your models here.

class MenuSectionAdmin(SummernoteModelAdmin):

    list_display = ['title']

@admin.register(MenuItem)

class MenuItemAdmin(SummernoteModelAdmin):

    list_display = ('title', 'ingredients', 'description', 'image', 'price')
    search_fields = ['title']
    summernote_fields = ('ingredients', 'description')