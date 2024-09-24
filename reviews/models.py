from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    body = models.TextField(max_length=5000)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Review {self.body} by {self.author}"