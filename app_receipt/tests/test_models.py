from django.test import TestCase
from django.contrib.auth.models import User
from app_receipt.models import Receipt
from datetime import date

class ReceiptModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_receipt(self):
        # Create a receipt instance
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase=date(2023, 12, 12),
            item_list='Test Item 1, Test Item 2, Test Item 3',
            total_amount=1000,
        )

        # Retrieve the receipt from the database
        saved_receipt = Receipt.objects.get(pk=receipt.pk)

        # Check if the saved receipt matches the created receipt
        self.assertEqual(saved_receipt.user, self.user)
        self.assertEqual(saved_receipt.store_name, 'Test Store')
        self.assertEqual(saved_receipt.date_of_purchase, date(2023, 12, 12))
        self.assertEqual(saved_receipt.item_list, 'Test Item 1, Test Item 2, Test Item 3')
        self.assertEqual(saved_receipt.total_amount, 1000)

    def test_receipt_str_representation(self):
        # Create a receipt instance
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase=date(2023, 12, 12),
            item_list='Test Item 1, Test Item 2, Test Item 3',
            total_amount=1000,
        )

        # Check if the string representation is as expected
        expected_str = 'Test Store - 2023-12-12'
        self.assertEqual(str(receipt), expected_str)
