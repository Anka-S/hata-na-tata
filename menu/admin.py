from django.contrib import admin
from .models import MenuSection, MenuItem
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MenuSection)

# Register your models here.

class MenuSectionAdmin(SummernoteModelAdmin):

    list_display = ['title']

@admin.register(MenuItem)

class MenuItemAdmin(SummernoteModelAdmin):

    list_display = ('title', 'ingredients', 'price', 'section', 'created_on')
    search_fields = ['title', 'ingredients']
    summernote_fields = ('description')
    list_filter = ['section', 'created_on']
    list_editable = ['price']

   