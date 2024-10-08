from django.test import TestCase
from django.urls import reverse
from .models import MenuSection, MenuItem

# Create your tests here.

class TestMenuView(TestCase):

    def setUp(self):
        self.menu_section = MenuSection.objects.create(title="Drinks")
        
        self.menu_item = MenuItem(section=self.menu_section,
            title="Compot",  ingredients="Berries and fruits", description="Sweet drink", price=4.00)
        self.menu_item.save()