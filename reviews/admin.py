from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review

@admin.register(Review)

# Register your models here.

class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'score', 'approved', 'created_on')
    summernote_fields = ('body')
    list_filter = ['created_on']
    