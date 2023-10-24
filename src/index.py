'''Käynnistää sovelluksen'''
import ui
from datetime import datetime
import lz78
import filecmp

def main():
    ui.start()

def run_lz78():
    start = datetime.now()
    with open('input.txt') as input_file:
        input_string = input_file.read()

    output_string = lz78.compress(input_string)
    print('Kirjoitetaan...')
    with open('output.bin','wb') as output_file:
        output_file.write(output_string)
    print(datetime.now()-start)

def lz78_decompress():
    start = datetime.now()
    with open('output.bin', 'rb') as file:
        data = file.read()

    decompressed = lz78.decompress(data)

    with open('decompressed.txt', 'w') as file:
        file.write(decompressed)

    print(datetime.now()-start)
    print(filecmp.cmp('input.txt', 'decompressed.txt', False))

if __name__ == '__main__':
    main()
