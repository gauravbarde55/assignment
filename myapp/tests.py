# myapp/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.client = APIClient()
        self.invoice_data = {'date': '2023-01-01', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Item', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_get_invoices(self):
        # Test GET /invoices/
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for other API endpoints

