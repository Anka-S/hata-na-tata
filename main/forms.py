from .models import Booking 
from django import forms 

class BookingForm(forms.ModelForm):     
    class Meta:       
         model = Booking        
         fields = ['name', 'email', 'date', 'time', 'guests', 'phone']

         widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-input-field'})