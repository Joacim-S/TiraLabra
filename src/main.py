'''Moduuli, jolla algoritmeja käytetään.'''
import lz78
from datetime import datetime

def run_lz78():
    start = datetime.now()
    with open('input.txt') as input_file:
        input_string = input_file.read()

    output_string = lz78.compress(input_string)
    print('Kirjoitetaan...')
    with open('output.bin','wb') as output_file:
        output_file.write(output_string)
    print(datetime.now()-start)

run_lz78()