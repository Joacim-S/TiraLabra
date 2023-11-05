'''Testaa lz78 algoritmia.'''
import unittest
from lz78 import Lz78


class TestLZ78(unittest.TestCase):
    '''Testaa lz78 algoritmia.'''

    def setUp(self):
        self.lz = Lz78()

    def test_generate_output_palauttaa_odotetun_listan(self):
        result = self.lz._generate_output('testi')
        self.assertEqual(result, ['01110100', '0', '01100101', '00', '01110011', '01', '01101001'])
        result = self.lz._generate_output('aa')
        self.assertEqual(result, ['01100001', '1'])

    def test_pakatun_syötteen_purku_tuottaa_alkuperäisen_syötteen(self):
        text = 'Tällä tekstillä testataan, saadaanko sen pakattu versio palautettua alkuperäiseksi'
        compressed = self.lz.compress(text)
        self.assertEqual(text, self.lz.decompress(compressed))
        text = 'aaa'
        compressed = self.lz.compress(text)
        self.assertEqual(text, self.lz.decompress(compressed))
        