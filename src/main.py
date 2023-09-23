'''Moduuli, jolla algoritmeja käytetään.'''
import lz78

with open('src/input.txt') as input_file:
    input_string = input_file.read()

output_string = lz78.compress(input_string)
with open('src/output.txt','w') as output_file:
    output_file.write(output_string)
