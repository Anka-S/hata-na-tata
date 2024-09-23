from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MenuPage(TemplateView):
    """
    Displays menu page
    """
    template_name = 'menu/menu.html'
