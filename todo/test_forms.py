from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # Create a form with a blank name field
        form = ItemForm({'name': ''})
        # Check if the form is invalid
        self.assertFalse(form.is_valid())
        # Check if the name field has the correct error
        self.assertIn('name', form.errors.keys())
        # Check if the error message is correct
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Create a form with a blank name field
        form = ItemForm({'name': 'Test Todo Item'})
        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # Create a form with a blank name field
        form = ItemForm()
        # Check if the form has the correct fields
        self.assertEqual(form.Meta.fields, ['name', 'done'])