from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenuSection(models.Model):
    title = models.CharField(max_length=200, unique=True)

class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name="section")
    title = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to='', storage=None, max_length=100, unique=True)
    ingredients = models.TextField(max_length=5000)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=3, decimal_places=3)
    # order = models.IntegerField(default=0)
    class Meta:        
        ordering = ['section']
    def __str__(self):        
        return self.title

