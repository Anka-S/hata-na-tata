from django.shortcuts import render
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
    return render(request, 'menu.html', {'sections': sections})