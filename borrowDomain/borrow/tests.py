from django.test import TestCase
from .models import Borrow 
# Create your tests here.
class BorrowTestCase(TestCase):
    def setUp(self):
        b1 = Borrow.objects.create(titulo = "TEST1")
        b2 = Borrow.objects.create(titulo = "TEST2")
        return (b1,b2)

    def test_borrow_are_valid_instance(self):
        borrows_test = self.setUp()
        self.assertTrue(isinstance(borrows_test[0],Borrow))
        self.assertTrue(isinstance(borrows_test[1],Borrow))