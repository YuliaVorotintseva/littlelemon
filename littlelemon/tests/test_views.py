from django.test import TestCase
from django.urls import reverse

from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="ChocolateCake", price=120, inventory=100)
        Menu.objects.create(title="Cheesecake", price=100, inventory=100)

    def test_getall(self):
        url = reverse('restaurant/menu')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)
        self.assertEqual(Menu.objects.count(), 3)