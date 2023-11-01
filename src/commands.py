'''Suorittaa käyttäjän syöttämät komennot'''
# import filecmp
import os
from datetime import datetime

from huffman import Huffman
from lz78 import Lz78


def handle_compress(file: str, algo: str):
    '''Käsittelee pakkauskomennon

    Args:
        file (str): Pakattavan tiedoston nimi
        algo (str): Algoritmin lyhenne

    Returns:
        object or str: Suoritusaika tai virheilmoitus
    '''
    start = datetime.now()
    if not algo:
        print(handle_compress(file, 'lz'))
        print(handle_compress(file, 'h'))
        return datetime.now()-start

    if algo == 'lz':
        lz78 = Lz78()
        with open(f'./src/input/{file}', encoding='utf-8') as input_file:
            string = input_file.read()
        compressed_data = lz78.compress(string)
        filename = file.split('.')[0]
        with open(f'./src/output/compressed/{filename}_lz.bin', 'wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start

    if algo == 'h':
        huf = Huffman()
        with open(f'./src/input/{file}', encoding='utf-8') as input_file:
            string = input_file.read()
        compressed_data = huf.compress(string)
        filename = file.split('.')[0]
        with open(f'./src/output/compressed/{filename}_h.bin', 'wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start

    return 'virheellinen algo komento'


def handle_decompress(file: str):
    '''Käsittelee purkukomennon

    Args:
        file (str): Purettavan tiedoston nimi

    Returns:
        object: Suoritusaika
    '''

    start = datetime.now()
    with open(f'./src/output/compressed/{file}', 'rb') as data_file:
        data = data_file.read()

    if file.endswith('_lz.bin'):
        lz78 = Lz78()
        decompressed = lz78.decompress(data)

    elif file.endswith('_h.bin'):
        huf = Huffman()
        decompressed = huf.decompress(data)

    filename = file.split('.')[0]
    with open(f'./src/output/decompressed/{filename}.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(decompressed)

    return datetime.now()-start


def handle_list(direc: str):
    '''Listaa kansion tiedostot

    Args:
        dir (str): Kansion nimi

    Returns:
        list: Tiedostonimet
    '''
    if direc == 'input':
        return os.listdir(f'./src/{direc}')
    return os.listdir(f'./src/output/{direc}')


def file_exists(file: str):
    '''Tarkistaa, löytyykö tiedostoa

    Args:
        file (str): Tiedoston sijainti ja nimi

    Returns:
        Bool: True, jos tiedosto löytyy
    '''
    with open(file):
        return True
