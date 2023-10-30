'''Huffmanin koodauksella pakkaus ja purku'''
import heapq

import tools


class Huffman:
    '''Huffmanin koodauksesta vastaava luokka'''

    def __init__(self):
        self._output_list = []
        self._i = 0

    def compress(self, text=str):
        '''Pakkaa syötetyn merkkijonon Huffmanin koodauksella ja palauttaa datan tavuina'''
        self._output_list = []
        frequencies = self._get_frequencies(text)
        heap = self._get_heap(frequencies)
        tree = self._get_tree(heap)
        encodings = self._get_encodings(tree, {})
        self._encode(text, encodings)
        result = tools.to_bytes(self._output_list)
        self._output_list = []
        return result

    def decompress(self, data):
        '''Huffmanin koodauksen purku'''
        self._output_list = []
        data_string = tools.to_string(data)
        self._i = tools.get_start_of_data(data_string)
        root = self._reconstruct_tree(Node(), data_string)
        self._decode(data_string[self._i:], root)
        result = ''.join(self._output_list)
        self._output_list = []
        return result

    def _decode(self, data_string, root):
        node = root
        for bit in data_string:
            if bit == '0' and node.left:
                node = node.left
            if bit == '1' and node.right:
                node = node.right
            if node.char:
                self._output_list.append(node.char)
                node = root

    def _reconstruct_tree(self, node, data_string):
        bit = data_string[self._i]
        self._i += 1
        if bit == '1':
            chr_bits = tools.get_char_length(data_string[self._i:self._i+4])
            node.char = int(
                data_string[self._i:self._i+chr_bits], 2).to_bytes(chr_bits//8, 'big').decode()
            self._i += chr_bits
            return node
        if bit == '0':
            node.left = Node()
            self._reconstruct_tree(node.left, data_string)
            node.right = Node()
            self._reconstruct_tree(node.right, data_string)
            return node

    def _get_frequencies(self, text=str):
        '''Muodostaa sanakirjan merkkien frekvenssistä merkkijonossa'''
        frequencies = {}
        for char in text:
            if char not in frequencies:
                frequencies[char] = 1
            else:
                frequencies[char] += 1
        return frequencies

    def _get_heap(self, frequencies):
        '''Muodostaa pinon lehtiä syötetyistä merkki frekvenssi pareista'''
        f_list = []
        for char, freq in frequencies.items():
            f_list.append(Node(freq, char))
        heapq.heapify(f_list)

        return f_list

    def _get_encodings(self, root, dictionary, encoding=''):
        '''Hakee merkkien koodaukset muodostetusta Huffmanin puusta'''
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
        '''Muodostaa Huffmanin puun syötetystä pinosta. Palauttaa juuren'''
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

    def __str__(self):
        return str(self.char)

    def __gt__(self, other):
        return self.value > other.value
