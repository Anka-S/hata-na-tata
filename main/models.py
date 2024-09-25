from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

GUESTS_CHOICES = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6","6"),
)

TIME_CHOICES = (
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM")
)
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=11, default='', null=False, validators=[RegexValidator(r"^[0-9]+$", "You can put only numbers and '+' symbol!")])
    email = models.EmailField(null=False)
    day = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="6 PM")
    guests = models.CharField(max_length=50, choices=GUESTS_CHOICES, default="2")

    class Meta:
        ordering = ["-day"]
    def __str__(self):
        return f"{self.name} | {self.day} | {self.time}"