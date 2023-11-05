'''Testaa Huffmanin koodausta.'''
import unittest
from huffman import Huffman
import heapq


class TestLZ78(unittest.TestCase):
    '''Testaa Huffmanin koodausta.'''

    def setUp(self):
        self.h = Huffman()
        
    def test_get_frequencies_palauttaa_odotetun_sanakirjan(self):
        frequencies = self.h._get_frequencies('hahaa banaani')
        self.assertEqual(frequencies['h'], 2)
        self.assertEqual(frequencies[' '], 1)
        self.assertEqual(frequencies['a'], 6)
        self.assertEqual(frequencies['b'], 1)
        self.assertEqual(frequencies['i'], 1)
        self.assertEqual(frequencies['n'], 2)
        
    def test_get_heap_palauttaa_odotetun_pinon(self):
        frequencies = {'a': 12, 'b': 250, 'c': 1, 'd': 10}
        heap = self.h._get_heap(frequencies)
        for item in [('c', 1), ('d', 10), ('a', 12), ('b', 250)]:
            node = heapq.heappop(heap)
            self.assertEqual(item, (node.char, node.value))
            
    def test_get_encodings_ja_get_tree_toimivat_odotetusti(self):
        frequencies = {'a': 12, 'b': 250, 'c': 1, 'd': 10}
        heap = self.h._get_heap(frequencies)
        encodings = self.h._get_encodings(self.h._get_tree(heap), {})
        self.assertEqual(encodings['b'], '1')
        self.assertEqual(encodings['a'], '01')
        self.assertEqual(encodings['d'], '001')
        self.assertEqual(encodings['c'], '000')
        
    def test_get_encodings_ja_get_tree_toimivat_odotetusti_yhdellä_merkillä(self):
        frequencies = {'k': 1}
        heap = self.h._get_heap(frequencies)
        encodings = self.h._get_encodings(self.h._get_tree(heap), {})
        self.assertEqual(encodings['k'], '0')
        
    def test_encode_toimii(self):
        encodings = {'m': '1', 'ä': '01', 'ö': '001', 't': '000', 'e': '0001', 'n': '0000'}
        text = 'tämmöne'
        self.h._encode(text, encodings)
        for code, char in zip(self.h._output_list, text):
            self.assertEqual(code, encodings[char])
            
    def test_decode_toimii(self):
        frequencies = {'a': 12, 'b': 250, 'c': 1, 'd': 10}
        heap = self.h._get_heap(frequencies)
        root = self.h._get_tree(heap)
        self.h._decode('01010110101000001001', root)
        self.assertEqual(''.join(self.h._output_list), 'aaabaacdd')
        
    def test_pakatun_syötteen_purku_tuottaa_alkuperäisen_syötteen(self):
        text = 'Tämmösellä pätkällä testaillaan tällä kertää!1!1!!!'
        compressed = self.h.compress(text)
        self.assertEqual(text, self.h.decompress(compressed))
        
    def test_tyhjän_merkkijonon_pakkaus_ja_purku(self):
        text = ''
        compressed = self.h.compress(text)
        self.assertEqual(text, self.h.decompress(compressed))
