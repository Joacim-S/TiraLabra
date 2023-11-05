'''Suorittaa käyttäjän syöttämät komennot'''
import os
import csv
from datetime import datetime

from huffman import Huffman
from lz78 import Lz78


def handle_compress_stats():
    '''Luo tilastotiedoston ja kutsuu hande_compress funktiota

    Returns:
        object: Suoritusaika
    '''
    num = 0
    while True:
        try:
            with open(f'./src/output/stats/stats_{num}.csv', 'x', encoding='utf-8') as stat_file:
                break
        except FileExistsError:
            num += 1
    with open(f'./src/output/stats/stats_{num}.csv', 'a', encoding='utf-8') as stat_file:
        writer = csv.writer(stat_file)
        writer.writerow(['file', 'original', 'LZ78', 'Huffman', 'LZ78_wins'])
    return handle_compress(stats=f'stats_{num}.csv')


def handle_compress(file: str = '', algo: str = '', stats: str = ''):
    '''Käsittelee pakkauskomennon

    Args:
        file (str): Pakattavan tiedoston nimi
        algo (str): Algoritmin lyhenne
        stats (str): Tiedosto, johon tilastot kirjoitetaan. '' = ei luoda tilastoa

    Returns:
        object or str: Suoritusaika tai virheilmoitus
    '''
    if algo and algo not in ('lz', 'h'):
        print('virheellinen komento')
        return 0

    start = datetime.now()
    if not file:
        files = handle_list('input')
        for i, fil in enumerate(files):
            print(
                f'Pakkaus suoritettu ajassa {handle_compress(fil, algo, stats)}')
            print(f'{i+1}/{len(files)} tiedostoa käsitelty')
        return datetime.now()-start

    if not algo:
        lz_result = handle_compress(file, "lz")
        print(f'lz78 pakkaus suoritettu ajassa {lz_result[0]}')
        h_result = handle_compress(file, "h")
        print(f'Huffman koodaus suoritettu ajassa {h_result[0]}')
        if stats:
            og_size = os.stat(f'./src/input/{file}').st_size
            with open(f'./src/output/stats/{stats}', 'a') as stat_file:
                writer = csv.writer(stat_file)
                writer.writerow([file, og_size, f'{(lz_result[1]/og_size):.2f}',
                                f'{(h_result[1]/og_size):.2f}', lz_result[1] <= h_result[1]])
        return datetime.now()-start

    if algo == 'lz':
        lz78 = Lz78()
        with open(f'./src/input/{file}', encoding='utf-8') as input_file:
            string = input_file.read()
        compressed_data = lz78.compress(string)
        filename = file.split('.')[0]
        with open(f'./src/output/compressed/{filename}_lz.bin', 'wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start, os.stat(f'./src/output/compressed/{filename}_lz.bin').st_size

    huf = Huffman()
    with open(f'./src/input/{file}', encoding='utf-8') as input_file:
        string = input_file.read()
    compressed_data = huf.compress(string)
    filename = file.split('.')[0]
    with open(f'./src/output/compressed/{filename}_h.bin', 'wb') as output_file:
        output_file.write(compressed_data)
    return datetime.now()-start, os.stat(f'./src/output/compressed/{filename}_h.bin').st_size


def handle_decompress(file: str):
    '''Käsittelee purkukomennon

    Args:
        file (str): Purettavan tiedoston nimi

    Returns:
        object: Suoritusaika
    '''

    start = datetime.now()

    if not file:
        files = handle_list('compressed')
        for i, fil in enumerate(files):
            print(f'Purku suoritettu ajassa {handle_decompress(fil)}')
            print(f'{i+1}/{len(files)} tiedostoa käsitelty')
        return datetime.now()-start

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
        files = os.listdir(f'./src/{direc}')
    else:
        files = os.listdir(f'./src/output/{direc}')
    non_hiddens = []
    for file in files:
        if not file.startswith('.'):
            non_hiddens.append(file)
    return non_hiddens


def file_exists(file: str, command: str):
    '''Tarkistaa, löytyykö tiedostoa

    Args:
        file (str): Tiedoston sijainti ja nimi
        command (str): Käyttäjän syöttämä komento

    Returns:
        bool: True, jos tiedosto löytyy
    '''
    if command == 'decompress':
        with open(f'./src/output/decompressed/{file}'):
            return True

    with open(f'./src/input/{file}'):
        return True
