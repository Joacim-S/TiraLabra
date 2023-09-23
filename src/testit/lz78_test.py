'''Testaa lz78 algoritmia.'''
import unittest
import lz78

class TestLZ78(unittest.TestCase):
    '''Testaa lz78 algoritmia.'''
    def test_lz78_koodaa_oikein(self):
        '''Testaa koodauksen.'''
        self.assertEqual(lz78.compress('AABBA'), '0A1B0B1$')
