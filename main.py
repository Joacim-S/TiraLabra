import LZ78
'''Lukee input.txt sisällön ja antaa sen LZ78 algoritmille, joka palauttaa koodatun tekstin. Se kirjoitetaan output.txt tiedostoon.
Etenkin tämän tiedoston rakenne tulee muuttumaan.'''
input_file = open('input.txt')
input_string = input_file.read()
input_file.close()
output_string = LZ78.compress(input_string)
output_file = open('output.txt','w')
output_file.write(output_string)
output_file.close()