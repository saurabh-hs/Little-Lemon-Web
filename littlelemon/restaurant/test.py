from django.test import TestCase
from restaurant.models import MenuTable
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="VainllaIce", price=80, inventory=100)
        self.assertEqual(str(item), "VainllaIce : 80")
        
class MenuViewTest(TestCase):
    def setUp(self):
        # create test menu items
        MenuTable.objects.create(title="Pizza", price=12.50, inventory=10)
        MenuTable.objects.create(title="Burger", price=8.00, inventory=25)
        MenuTable.objects.create(title="Pasta", price=10.00, inventory=15)

    def test_getall(self):
        url = reverse("menu-list")  # <-- name from your urls.py
        response = self.client.get(url)

        menus = MenuTable.objects.all()
        serialized = MenuItemSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized.data)