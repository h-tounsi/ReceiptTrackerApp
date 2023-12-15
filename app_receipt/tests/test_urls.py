from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_receipt.views import register_page , login_page, logout_page, receipt_list , receipt_detail, receipt_new, receipt_edit, receipt_delete , receipt_delete_selected



class TestUrls(SimpleTestCase):

    # RegisterPage TestUrl
    def test_register_page_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_page)

    # LoginPage TestUrl
    def test_login_page_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_page)

    # LogoutPage TestUrl
    def test_logout_page_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_page)

    # ReceiptList TestUrl
    def test_receipt_list_url_is_resolved(self):
        url = reverse('receipt_list')
        self.assertEqual(resolve(url).func, receipt_list)

    # ReceiptDetail TestUrl
    def test_receipt_detail_url_is_resolved(self):
        url = reverse('receipt_detail', args=[1])
        self.assertEqual(resolve(url).func, receipt_detail)
    
    # ReceiptNew TestUrl
    def test_receipt_new_url_is_resolved(self):
        url = reverse('receipt_new')
        self.assertEqual(resolve(url).func, receipt_new)
    
    # ReceiptEdit TestUrl
    def test_receipt_edit_url_is_resolved(self):
        url = reverse('receipt_edit', args=[1])
        self.assertEqual(resolve(url).func, receipt_edit)

    # ReceiptDelete TestUrl
    def test_receipt_delete_url_is_resolved(self):
        url = reverse('receipt_delete', args=[1])
        self.assertEqual(resolve(url).func, receipt_delete)

    # ReceiptDeleteSelected TestUrl
    def test_receipt_delete_selected_url_is_resolved(self):
        url = reverse('receipt_delete_selected')
        self.assertEqual(resolve(url).func, receipt_delete_selected)

    
