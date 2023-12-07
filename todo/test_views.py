from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    
    def test_get_todo_list(self):
        # Create a response variable that stores the response from the client
        response = self.client.get('/')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_get_add_item_page(self):
        # Create a response variable that stores the response from the client
        response = self.client.get('/add')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_item_page(self):
        # Create an item
        item = Item.objects.create(name='Test Todo Item')
        # Create a response variable that stores the response from the client
        response = self.client.get(f'/edit/{item.id}')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        # Create a response variable that stores the response from the client
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # Check if the status code is 200
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        # Create an item
        item = Item.objects.create(name='Test Todo Item')
        # Create a response variable that stores the response from the client
        response = self.client.get(f'/delete/{item.id}')
        # Check if the status code is 200
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        # Create an item
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Create a response variable that stores the response from the client
        response = self.client.get(f'/toggle/{item.id}')
        # Check if the status code is 200
        self.assertRedirects(response, '/')
        # Get the item again from the database
        updated_item = Item.objects.get(id=item.id)
        # Check if the item is done
        self.assertFalse(updated_item.done)
        
    def test_can_edit_item(self):
        # Create an item
        item = Item.objects.create(name='Test Todo Item')
        # Create a response variable that stores the response from the client
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # Check if the status code is 200
        self.assertRedirects(response, '/')
        # Get the item again from the database
        updated_item = Item.objects.get(id=item.id)
        # Check if the item name is updated
        self.assertEqual(updated_item.name, 'Updated Name')    
