from .models import Booking 
from django import forms 
import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'day', 'time', 'guests', 'phone']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(attrs={'class': 'form-input-field'}),
            'guests': forms.Select(attrs={'class': 'form-input-field'}),
        }

    def clean_day(self):
        day = self.cleaned_data.get('day')
        today = date.today()
        if day < today:
            raise forms.ValidationError('Date cannot be in the past.')
        if day > today + timedelta(days=30):
            raise forms.ValidationError('Date cannot be more than 30 days in the future.')
        return day

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['email'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['phone'].widget.attrs.update({'class': 'form-input-field'})

    def clean_day(self):
        day = self.cleaned_data.get('day')
        if day < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return day