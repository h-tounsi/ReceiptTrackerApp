from django.test import TestCase
from app_receipt.forms import ReceiptForm, UserCreationForm

class FormsTest(TestCase):

    def test_receipt_form(self):
        form_data = {
            'store_name': 'Test Store',
            'date_of_purchase': '2023-12-12',
            'item_list': 'Test Item 1, Test Item 2, Test Item 3',
            'total_amount': 1000,
        }
        form = ReceiptForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_user_creation_form(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = UserCreationForm(data=form_data)

        self.assertTrue(form.is_valid())

# Path: app_receipt/tests/test_urls.py
        
