from django.test import TestCase
from .models import Borrow 
import datetime
# Create your tests here.
class BorrowTestCase(TestCase):
    def setUp(self):
        id_sol = 1
        id_pres = 1
        fecha_ini = datetime.date.today() 
        fecha_fin = datetime.date(2025,12, 3)
        b1 = Borrow.objects.create(id_solicitante = id_sol,id_prestamista = id_pres, fecha_inicio = fecha_ini, fecha_termino = fecha_fin )
        return b1

    def test_borrow_are_valid_instance(self):
        borrows_test = self.setUp()
        self.assertTrue(isinstance(borrows_test,Borrow))
        
    
    def create_borrow_object(self):
        borrow = Borrow(1000,1000,datetime.date.today(),datetime.date(2030,12,5))
        Borrow.save(borrow)
        borrow_db = Borrow.objects.get(id_prestamista = 1000)
        self.assertEqual(borrow,borrow_db)


