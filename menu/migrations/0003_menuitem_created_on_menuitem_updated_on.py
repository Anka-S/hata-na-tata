# Generated by Django 4.2.16 on 2024-09-23 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]