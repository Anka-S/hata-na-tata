# import re
from django.contrib import admin
from .models import MenuSection, MenuItem
# from django.utils.html import strip_tags, format_html
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


    # def clean_ingredients(self, obj):
    #     clean_text = strip_tags(obj.ingredients)
    #     clean_text = re.sub(r'\s+', ' ', clean_text)
    #     clean_text = clean_text.strip()
    #     return (clean_text[:200] + ' ... ') if len(clean_text) > 200 else clean_text
    # clean_ingredients.short_description = 'Ingredients'

   