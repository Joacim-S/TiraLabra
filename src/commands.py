import filecmp
import os
from lz78 import compress, decompress
from datetime import datetime

def handle_compress(file, algo):
    start = datetime.now()
    if not algo:
        print('molemmat')

    if algo == 'lz':
        with open(f'input/{file}') as input_file:
            string = input_file.read()
        compressed_data = compress(string)
        filename = file.split('.')[0]
        with open(f'output/compressed/{filename}_lz.bin','wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start

    if algo == 'h':
        print('huffman')

    print('virheellinen algo komento')
    

def handle_decompress(file):
    start = datetime.now()
    with open(f'output/compressed/{file}', 'rb') as data_file:
        data = data_file.read()

    if file.endswith('_lz.bin'):
        decompressed = decompress(data)

    filename = file.split('.')[0]
    with open(f'output/decompressed/{filename}.txt', 'w') as output_file:
        output_file.write(decompressed)

    return datetime.now()-start

def handle_list(dir):
    if dir == 'input':
        return os.listdir(dir)
    return os.listdir(f'output/{dir}')

def file_exists(file):
    with open(file) as text_file:
        return True
    