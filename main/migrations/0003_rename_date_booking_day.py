# Generated by Django 4.2.16 on 2024-09-25 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_booking_table_booking_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='day',
        ),
    ]
