from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'main/index.html'

@login_required
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
            messages.error(
                    request,
                    'You put incorrect values, please check all fields')
    context = {
        'form': form,
    }
    return render(request, 'main/booking.html', context)
