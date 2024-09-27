from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from django.core.exceptions import ValidationError




# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'main/index.html'

def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            Booking = form.save(commit=False)
            Booking.user = request.user
            Booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('home')
        else:
            messages.error(request, 'You put incorrect values, please check all fields')
  
        
    context = {
        'form': form,
    }
    return render(request, 'main/booking.html', context)

