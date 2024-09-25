from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'main/index.html'

def home(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('home')
    else:
        form = BookingForm()
    
    return render(request, 'index.html', {'form': form})
