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

def validate_date(value):
    today = date.today()
    if value < today:
        raise ValidationError('Date cannot be in the past.')
    if value > today + timedelta(days=30):
        raise ValidationError('Date cannot be more than 30 days in the future.')

def home(request):
    print(f"Request method: {request.method}")
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        # print(f"Form is valid: {form.is_valid()}")
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('home')
    else:
        print(f"Form errors: {form.errors}")
        
    
    context = {
        'form': form,
    }
    return render(request, 'main/index.html', context)

@login_required
def booking(request):
    # Your existing booking view logic here
    pass