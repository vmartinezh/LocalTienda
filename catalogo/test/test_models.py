import unittest
import mymodule
from django.test import TestCase
from catalogo.models import Prenda

# Create your tests here.
class PrendaModelTest(TestCase):

    @classmethod
    def test_desc(self):
        defi=Prenda.descripcion.max_length
        max_length = defi._meta.get_field('descri').max_length
        self.assertNotEqual(max_length,200)
   
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)

    def test_get_prime_numbers(self):
        self.assertEqual(mymodule.get_prime_numbers(10), [2, 3, 5, 7]


