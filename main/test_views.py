from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking
from .forms import BookingForm

# Create your tests here.
class TestBookingView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="myUsername", password="myPassword")


    def test_successful_booking(self):
        
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'name': 'name', 'email':'testemail@mail.ru', 'day':'2024-10-02', 'time':'5 PM', 'guests':'3', 'phone':'07555555555'}
        response = self.client.post(reverse('booking'), data=post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Booking successful!')


