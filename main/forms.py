from .models import Booking 
from django import forms 
from django.core.validators import MinLengthValidator
from datetime import datetime, timedelta

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'day', 'time', 'guests', 'phone']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'date', 'id':'id_day'}),
            'time': forms.Select(attrs={'class': 'form-input-field'}),
            'guests': forms.Select(attrs={'class': 'form-input-field'}),
            'phone': forms.TextInput(attrs={'id': 'id_phone'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['email'].widget.attrs.update({'class': 'form-input-field'})
        self.fields['phone'].validators.append(MinLengthValidator(11))
    
    def clean_day(self):
        day = self.cleaned_data.get('day')
        today = day.today()
        if day < today:
            raise forms.ValidationError('You cannot choose a date in the past.')
        if day > today + timedelta(days=30):
            raise forms.ValidationError('Please, choose a date less than 30 days in the future.')
        return day
    
    
