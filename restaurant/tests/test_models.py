from django.test import TestCase, Client
from ..models import Menu
from ..serializers import MenuSerializer

# Create your tests here.
class MenuTest(TestCase):
    def test_str(self):
        item = Menu.objects.create(title="Fried Rice", price=50.00, inventory=30)
        itemstr = item.__str__()

        self.assertEqual(itemstr, "Fried Rice : 50.00")
