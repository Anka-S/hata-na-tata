from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuPage.as_view(), name='menu')
]