# Generated by Django 4.2.16 on 2024-09-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
