from django.test import TestCase
from django.urls import reverse
import transaction.tests.constants as constants

class TestTransactionAppUrls(TestCase):
    USER_ID = constants.USER_ID
    TRANSACTION_ID = constants.TRANSACTION_ID

    def test_resolution_for_transaction_list(self):        
        url = reverse('transaction:list',kwargs={'user':self.USER_ID})
        self.assertEqual(url, constants.URL_TRANSACTION.format(self.USER_ID))

    def test_resolution_for_expenses_summary(self):        
        url = reverse('transaction:expenses_summary',kwargs={'user':self.USER_ID})
        self.assertEqual(url, constants.URL_TRANSACTION.format(self.USER_ID)+constants.EXPENSES_SUMMARY)

    def test_resolution_for_summary(self):        
        url = reverse('transaction:summary',kwargs={'user':self.USER_ID})
        self.assertEqual(url, constants.URL_TRANSACTION.format(self.USER_ID)+constants.SUMMARY)

    def test_resolution_for_balance(self):        
        url = reverse('transaction:balance',kwargs={'user':self.USER_ID})
        self.assertEqual(url, constants.URL_TRANSACTION.format(self.USER_ID)+constants.BALANCE)

    def test_resolution_for_transaction_detail(self):        
        url = reverse('transaction:detail',kwargs={'user':self.USER_ID, 'pk': self.TRANSACTION_ID})
        self.assertEqual(url, constants.URL_DETAIL.format(self.USER_ID, self.TRANSACTION_ID))