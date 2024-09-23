# Generated by Django 4.2.16 on 2024-09-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.FileField(unique=True, upload_to='')),
                ('ingredients', models.TextField(max_length=5000)),
                ('description', models.TextField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=3, max_digits=3)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='menu.menusection')),
            ],
            options={
                'ordering': ['section'],
            },
        ),
    ]
