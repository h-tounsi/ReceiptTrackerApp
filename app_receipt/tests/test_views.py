from django.test import TestCase , Client
from django.urls import reverse
from app_receipt.models import Receipt
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):

        # Define urls
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.receipt_list_url = reverse('receipt_list')
        self.receipt_new_url = reverse('receipt_new')
        self.receipt_delete_selected_url = reverse('receipt_delete_selected')

   
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )

        # Login the user
        self.client.login(
            username='testuser', 
            password='testpassword'
        )

        # Create a receipt for testing
        self.receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-12-12',
            item_list='Test Item 1, Test Item 2, Test Item 3',
            total_amount=1000,
        )

    # Test the register page
    def test_register_page(self):

        # Test GET request to the register page
        response_get = self.client.get(self.register_url)
        self.assertIn(response_get.status_code, [200, 302])
        if response_get.status_code == 200:
            self.assertTemplateUsed(response_get, 'register.html')
        else:
            self.assertRedirects(response_get, self.receipt_list_url)

        # Test POST request to register a new user
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'}
        response_post = self.client.post(self.register_url, data, follow=True)

        # Check if the user was created
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Check if the response redirects to the correct location after registration
        self.assertRedirects(response_post, self.receipt_list_url)

        # Create a user and log them in
        User.objects.create_user(username='existinguser', password='existingpassword')
        self.client.login(username='existinguser', password='existingpassword')

        # Attempt to access the register page while authenticated
        response_authenticated = self.client.get(self.register_url)

        # Check if the user is redirected to the receipt_list page
        self.assertRedirects(response_authenticated, self.receipt_list_url)

    # Test the login page
    def test_login_page(self):
        # Test GET request to the login page
        response = self.client.get(self.login_url)
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 200:
            self.assertTemplateUsed(response, 'login.html')
        else:
            # If redirected, assert that the redirection is expected
            self.assertRedirects(response, self.receipt_list_url)

        # Test POST request with valid login credentials
        data_valid = {'username': 'testuser', 'password': 'testpassword'}
        response_valid = self.client.post(self.login_url, data_valid, follow=True)
        self.assertRedirects(response_valid, self.receipt_list_url)

        # Test POST request with invalid login credentials
        data_invalid = {'username': 'testuser', 'password': 'wrongpassword'}
        response_invalid = self.client.post(self.login_url, data_invalid, follow=True)
        self.assertEqual(response_invalid.status_code, 200)
        self.assertRaisesMessage(response_invalid, 'Incorrect username or password.')
       

        
        # Test accessing the login page when already authenticated
        self.client.login(username='testuser', password='testpassword')
        response_authenticated = self.client.get(self.login_url)
        self.assertRedirects(response_authenticated, self.receipt_list_url)

    # Test the logout page
    def test_logout_page(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the logout page
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, self.login_url)

        # Log out the user
        self.client.logout()

    # Test the receipt_list page
    def test_receipt_list_view(self):
        response = self.client.get(reverse('receipt_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipt_list.html')

    # Test the receipt_new page
    def test_receipt_new_view(self):
        response = self.client.get(self.receipt_new_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipt_new.html')

        data = {
            'store_name': 'Receipt 1',
            'date_of_purchase': '2023-12-14',
            'item_list': 'Test Item 1, Test Item 2',
            'total_amount': 100,
        }
        response_post = self.client.post(self.receipt_new_url, data)
        self.assertEqual(response_post.status_code, 302)  
        self.assertRedirects(response_post, self.receipt_list_url)

    # Test the receipt_detail page
    def test_receipt_detail_view(self):
        response = self.client.get(reverse('receipt_detail', args=[self.receipt.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipt_detail.html')

    # Test the receipt_edit page
    def test_receipt_edit_view(self):
        response = self.client.get(reverse('receipt_edit', args=[self.receipt.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipt_edit.html')

        data = {
            'store_name': 'Updated Receipt',
            'date_of_purchase': '2023-12-14',
            'item_list': 'Test Item 1, Test Item 2',
            'total_amount': 100,
        }
        response_post = self.client.post(reverse('receipt_edit', args=[self.receipt.pk]), data)
        self.assertEqual(response_post.status_code, 302) 
        self.assertRedirects(response_post, reverse('receipt_detail', args=[self.receipt.pk]))

    # Test the receipt_delete page
    def test_receipt_delete_view(self):
        response = self.client.post(reverse('receipt_delete', args=[self.receipt.pk]))
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, self.receipt_list_url)

    # Test the receipt_delete_selected page
    def test_receipt_delete_selected_view(self):
        response = self.client.post(self.receipt_delete_selected_url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, self.receipt_list_url)


