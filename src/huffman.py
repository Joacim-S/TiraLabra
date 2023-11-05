'''Huffmanin koodauksella pakkaus ja purku'''
import heapq

import tools


class Huffman:
    '''Huffmanin koodauksesta vastaava luokka'''

    def __init__(self):
        self._output_list = []
        self._i = 0

    def compress(self, text: str):
        '''Pakkaa syötteen Huffmanin koodauksella

        Args:
            text (str): pakattava merkkijono

        Returns:
            bytearray: Pakattu data tavuina
        '''
        self._output_list = []
        if len(text) == 0:
            return tools.to_bytes(text)
        frequencies = self._get_frequencies(text)
        heap = self._get_heap(frequencies)
        tree = self._get_tree(heap)
        encodings = self._get_encodings(tree, {})
        self._encode(text, encodings)
        return tools.to_bytes(self._output_list)

    def decompress(self, data: str):
        '''Purkaa Huffman koodatun syötteen

        Args:
            data (str): purettava data

        Returns:
            str: Purettu merkkijono
        '''
        self._output_list = []
        data_string = tools.to_string(data)
        self._i = tools.get_start_of_data(data_string)
        if self._i >= len(data_string):
            return ''.join(self._output_list)
        root = self._reconstruct_tree(Node(), data_string)
        self._decode(data_string[self._i:], root)
        return ''.join(self._output_list)

    def _decode(self, data_string: str, root: object):
        '''Purkaa Huffman koodauksen

        Args:
            data_string (str): Huffman koodattu merkkijono
            root (object): Huffman puun juuri
        '''
        node = root
        for bit in data_string:
            if bit == '0' and node.left:
                node = node.left
            if bit == '1' and node.right:
                node = node.right
            if node.char:
                self._output_list.append(node.char)
                node = root

    def _reconstruct_tree(self, node: object, data_string: str):
        '''Rakentaa Huffman koodauksessa käytetyn puun

        Args:
            node (object): Käsiteltävä solmu
            data_string (str): Merkkijono, jonka alussa puun rakennusohja

        Returns:
            object: Käsitelty solmu
        '''
        bit = data_string[self._i]
        self._i += 1
        if bit == '1':
            chr_bits = tools.get_char_length(data_string[self._i:self._i+4])
            node.char = int(
                data_string[self._i:self._i+chr_bits], 2).to_bytes(chr_bits//8, 'big').decode()
            self._i += chr_bits
            return node

        node.left = Node()
        self._reconstruct_tree(node.left, data_string)
        node.right = Node()
        self._reconstruct_tree(node.right, data_string)
        return node

    def _get_frequencies(self, text: str):
        '''Laskee merkkien esiintymiskerrat syötteessä

        Args:
            text (str): Käsiteltävä merkkijono

        Returns:
            dict: Sanakirja merkki:esiintymiskerrat pareista
        '''
        frequencies = {}
        for char in text:
            if char not in frequencies:
                frequencies[char] = 1
            else:
                frequencies[char] += 1
        return frequencies

    def _get_heap(self, frequencies: dict):
        '''Muodostaa minipinon solmuja merkeistä ja niiden esiintymiskerroista

        Args:
            frequencies (dict): Merkki:esiintymiskerrat sanakirja

        Returns:
            heap: Pino solmuja merkeistä ja niiden esiintymiskerroista
        '''
        f_list = []
        for char, freq in frequencies.items():
            f_list.append(Node(freq, char))
        heapq.heapify(f_list)

        return f_list

    def _get_encodings(self, root: object, dictionary: dict, encoding: str = ''):
        '''Hakee merkkien koodaukset ja tallentaa puun output_listiin

        Args:
            root (object): Huffman puun juuri
            dictionary (dict): merkki:koodaus sanakirja
            encoding (str, optional): Merkin koodauksen aiemmat merkit. Defaults to ''.

        Returns:
            dict: valmis merkki:koodaus sanakirja
        '''
        if root.char:
            self._output_list.append('1')
            char = root.char.encode()
            for byte in char:
                self._output_list.append(bin(byte)[2:].zfill(8))
            if encoding == '':
                encoding = '0'
            dictionary[root.char] = encoding
        else:
            self._output_list.append('0')
        if root.left:
            self._get_encodings(root.left, dictionary, f'{encoding}0')
        if root.right:
            self._get_encodings(root.right, dictionary, f'{encoding}1')
        return dictionary

    def _get_tree(self, heap):
        '''Muodostaa Huffman puun solmupinosta

        Args:
            heap (heap): Pino solmuja

        Returns:
            object: Huffman puun juuri
        '''
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            root = Node(left.value+right.value, None, left, right)
            heapq.heappush(heap, root)
        return heapq.heappop(heap)

    def _encode(self, text, encodings):
        for char in text:
            self._output_list.append(encodings[char])


class Node:
    '''Puun solmuista vastaava luokka'''

    def __init__(self, value=0, char=None, left=None, right=None):
        self.value = value
        self.char = char
        self.left = left
        self.right = right

    def __gt__(self, other):
        return self.value > other.value
