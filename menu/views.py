from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from .models import MenuSection, MenuItem


# Create your views here.

class MenuPage(TemplateView):
    """
    Displays menu page
    """
    template_name = 'menu/menu.html'

def menu_view(request):     
    menu_sections = MenuSection.objects.all()
    menu_items = MenuItem.objects.all().select_related('section')  

    print(f"Sections: {menu_sections.count()}")
    print(f"Items: {menu_items.count()}")

    context = {
        "menu_sections" : menu_sections,
        "menu_items" : menu_items,
    } 
    return render(request, 'menu/menu.html', context)