import filecmp
import os
from datetime import datetime

from huffman import Huffman
from lz78 import Lz78

def handle_compress(file, algo):
    start = datetime.now()
    if not algo:
        print(handle_compress(file, 'lz'))
        print(handle_compress(file, 'h'))
        return datetime.now()-start

    if algo == 'lz':
        lz = Lz78()
        with open(f'./src/input/{file}') as input_file:
            string = input_file.read()
        compressed_data = lz.compress(string)
        filename = file.split('.')[0]
        with open(f'./src/output/compressed/{filename}_lz.bin','wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start

    if algo == 'h':
        h = Huffman()
        with open(f'./src/input/{file}') as input_file:
            string = input_file.read()
        compressed_data = h.compress(string)
        filename = file.split('.')[0]
        with open(f'./src/output/compressed/{filename}_h.bin','wb') as output_file:
            output_file.write(compressed_data)
        return datetime.now()-start

    print('virheellinen algo komento')
    

def handle_decompress(file):
    start = datetime.now()
    with open(f'./src/output/compressed/{file}', 'rb') as data_file:
        data = data_file.read()

    if file.endswith('_lz.bin'):
        lz = Lz78()
        decompressed = lz.decompress(data)

    elif file.endswith('_h.bin'):
        h = Huffman()
        decompressed = h.decompress(data)
        
    filename = file.split('.')[0]
    with open(f'./src/output/decompressed/{filename}.txt', 'w') as output_file:
        output_file.write(decompressed)

    return datetime.now()-start

def handle_list(dir):
    if dir == 'input':
        return os.listdir(f'./src/{dir}')
    return os.listdir(f'./src/output/{dir}')

def file_exists(file):
    with open(file) as text_file:
        return True
    