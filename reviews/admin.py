from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review

@admin.register(Review)

# Register your models here.

class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_filter = ['created_on']