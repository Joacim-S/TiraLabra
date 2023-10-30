'''Testaa lz78 algoritmia.'''
import unittest
from lz78 import lz

class TestLZ78(unittest.TestCase):
    '''Testaa lz78 algoritmia.'''
    def setUp(self):
        self.lz = Lz78
        
    def test_lz78_koodaa_oikein(self):
        '''Testaa koodauksen.'''
        self.assertEqual(lz78.compress('AABBA'), '0A1B0B1$')

