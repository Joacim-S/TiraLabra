'''LZ78 algoritmilla pakkaus ja purku'''
import tools


class Lz78:
    '''Lz78:sta vastaava luokka
    '''

    def __init__(self):
        pass

    def compress(self, text: str):
        '''Pakkaa merkkijonon

        Args:
            text (str): Pakattava merkkijono

        Returns:
            bytearray: Pakattu data
        '''
        print('Pakataan...')
        output_list = self._generate_output(text)
        print('Muutetaan tavuiksi...')
        return tools.to_bytes(output_list)

    def decompress(self, data):
        '''Purkaa lz78 pakatun datan

        Args:
            data (str): Pakkauksen tuottama binäärimerkkijono

        Returns:
            str: Alkuperäinen merkkijono
        '''
        print('Luetaan dataa...')
        data_string = tools.to_string(data)
        output = []
        bits = 0
        segments = 0
        segment_limit = 0.5

        dictionary = ['']
        i = tools.get_start_of_data(data_string)
        next_index = 1

        print('Puretaan...')
        while i < len(data_string)-bits:
            previous = ''
            if bits:
                key = int(data_string[i:i+bits], 2)
                i += bits
                previous = dictionary[key]

            chr_bits = tools.get_char_length(data_string[i:i+4])
            next_char = int(data_string[i:i+chr_bits],
                            2).to_bytes(chr_bits//8, 'big').decode()
            segment = f'{previous}{next_char}'
            output.append(segment)
            dictionary.append(segment)
            next_index += 1
            i += chr_bits
            segments += 1
            if segments >= segment_limit:
                bits += 1
                segment_limit *= 2
                segments = 0
        print('Yhdistetään merkkijonoksi...')
        if i < len(data_string):
            output.append(dictionary[int(data_string[i:], 2)])
        return ''.join(output)

    def _generate_output(self, text: str):
        '''Pakkaa syötteen

        Args:
            text (str): Pakattava merkkijono

        Returns:
            list: Pakattu binäärimerkkijono listana
        '''
        last_match = 0
        next_index = 1
        i = 0
        dictionary = {(0, ''): 0}
        output = []
        bits = 0
        segments = 0
        segment_limit = 0.5
        added = False
        while i < len(text):
            key = (last_match, text[i])
            if key in dictionary:
                last_match = dictionary[key]
                i += 1
                added = False

            else:
                added = True
                dictionary[last_match, text[i]] = next_index
                next_index += 1
                if bits:
                    output.append(f'{last_match:0{bits}b}')
                char = text[i].encode()
                for byte in char:
                    output.append(bin(byte)[2:].zfill(8))
                last_match = 0
                i += 1
                segments += 1
                if segments >= segment_limit:
                    bits += 1
                    segment_limit *= 2
                    segments = 0
        if not added:
            output.append(f'{last_match:0{bits}b}')
        return output
