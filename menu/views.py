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
    sections = MenuSection.objects.all()
    items = MenuItem.objects.all()   
    return render(request, 'menu.html', {
        'sections': sections,
        'items': items,
        })