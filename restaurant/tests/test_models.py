from django.test import TestCase, Client
from ..models import Menu, Booking
from ..serializers import MenuSerializer

# Create your tests here.
class MenuTest(TestCase):
    def test_str(self):
        item = Menu.objects.create(title="Fried Rice", price=50.00, inventory=30)
        itemstr = item.__str__()

        self.assertEqual(itemstr, "Fried Rice : 50.00")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Fried Rice", price=50.00, inventory=30)
        Menu.objects.create(title="Jellof Rice", price=40.00, inventory=30)
        Menu.objects.create(title="Stew Rice", price=45.00, inventory=30)
        
        self.client = Client()

    def test_getall(self):
        # Make a GET request to the view url
        response = self.client.get('/restaurant/menu/')

        # check response status
        self.assertEqual(response.status_code, 200)

        # Retrieve all items from the database
        menu_items = Menu.objects.all()

        # Serialize the menu items
        serializer = MenuSerializer(menu_items, many=True)

        # Compare serialize data with response
        self.assertEqual(response.data, serializer.data)

        # Check total number of menu items
        self.assertEqual(len(response.data), menu_items.count())
