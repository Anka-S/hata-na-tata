from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ['user', 'name', 'phone', 'day', 'time', 'created_on']
    list_filter = ['day']
