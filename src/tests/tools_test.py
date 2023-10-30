'''Testaa tools moduulia'''
import unittest

import tools

class Testtools(unittest.TestCase):
    '''Testaa tools moduulia.'''

    def test_to_bytes_palauttaa_odotetyn_tavulistan(self):
        bytear = tools.to_bytes(['001010', '11', '011'])
        self.assertEqual(len(bytear), 2)
        self.assertEqual(bytear[0], 9)
        self.assertEqual(bytear[1], 91)

    def test_to_string_palauttaa_odotetun_merkkijonon(self):
        bytear = bytearray([1, 255, 0, 138, 95])
        self.assertEqual(tools.to_string(bytear),
                         '0000000111111111000000001000101001011111')

    def test_get_start_of_data_palauttaa_odotetun_indeksin(self):
        self.assertEqual(tools.get_start_of_data('00011000'), 4)

    def test_get_char_length_palauttaa_odotetun_arvon(self):
        self.assertEqual(tools.get_char_length('0000'), 8)
        self.assertEqual(tools.get_char_length('1100'), 16)
        self.assertEqual(tools.get_char_length('1110'), 24)
        self.assertEqual(tools.get_char_length('1111'), 32)
