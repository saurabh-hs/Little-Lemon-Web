from django.test import TestCase
from restaurant.models import MenuTable

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title="VainllaIce", price=80, inventory=100)
        self.assertEqual(str(item), "VainllaIce : 80")
#this is not a default location lol i places my tests in app lvl