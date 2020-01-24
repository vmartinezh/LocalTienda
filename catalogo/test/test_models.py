import unittest
from django.test import TestCase
from catalogo.models import Prenda

# Create your tests here.
class PrendaModelTest(TestCase):

    @classmethod
    def test_desc(self):
        defi=Prenda.descripcion.max_length
        max_length = defi._meta.get_field('descri').max_length
        self.assertEqual(max_length,200)

