'''LZ78 algoritmilla pakkaus ja purku'''
def compress(text=str):
    '''Pakkaa syötetyn merkkijonon LZ78 algoritmilla ja palauttaa datan tavuina'''
    print('Pakataan...')
    output_list = generate_output(text)
    print('Muutetaan tavuiksi...')
    return convert_to_bytes(output_list)

def generate_output(text=str):
    '''Pakkaa syötteen ja palauttaa pakatun datan listana'''
    last_match = 0
    next_index = 1
    i = 0
    dictionary = {(0, '') : 0}
    output = []
    bits = 0
    segments = 0
    segment_limit = 0.5
    added = False
    while i < len(text):
        key = (last_match, text[i])
        if key in dictionary:
            last_match = dictionary[key]
            i += 1
            added = False

        else:
            added = True
            dictionary[last_match, text[i]] = next_index
            next_index += 1
            if bits:
                output.append(f'{last_match:0{bits}b}')
            char = text[i].encode()
            for byte in char:
                output.append(bin(byte)[2:].zfill(8))
            last_match = 0
            i+=1
            segments += 1
            if segments >= segment_limit:
                bits += 1
                segment_limit *= 2
                segments = 0
    if not added:
        output.append(f'{last_match:0{bits}b}')
    return output


def convert_to_bytes(data=list):
    '''Muuttaa listana olevan datan kokonaisiksi tavuiksi'''
    output_string = ''.join(data)
    to_next_byte = 8 - len(output_string) % 8
    output_string_prefixed = f'{"0"*(to_next_byte-1)}1{output_string}'
    output_byte_list = []

    for i in range(0, len(output_string_prefixed), 8):
        output_byte_list.append(int(output_string_prefixed[i:i+8], 2))

    return bytearray(output_byte_list)


def decompress(data):
    '''Purkaa lz78:lla pakatun syötteen ja palauttaa alkuperäisen merkkijonon.'''
    print('Luetaan dataa...')
    data_string = convert_to_string(data)
    output = []
    bits = 0
    segments = 0
    segment_limit = 0.5

    dictionary = ['']
    i = 0
    next_index = 1

    while data_string[i] == '0':
        i += 1
    i += 1

    print('Puretaan...')
    while i < len(data_string)-bits:
        previous = ''
        if bits:
            key = int(data_string[i:i+bits], 2)
            i += bits
            previous = dictionary[key]

        chr_bits = 8
        for bit in data_string[i:i+4]:
            if bit == '0':
                break
            chr_bits += 8

        if chr_bits > 8:
            chr_bits -= 8
        next_char = int(data_string[i:i+chr_bits], 2).to_bytes(chr_bits//8, 'big').decode()
        segment = f'{previous}{next_char}'
        output.append(segment)
        dictionary.append(segment)
        next_index += 1
        i += chr_bits
        segments += 1
        if segments >= segment_limit:
            bits += 1
            segment_limit *= 2
            segments = 0
    print('Yhdistetään merkkijonoksi...')
    if i < len(data_string):
        output.append(dictionary[int(data_string[i:], 2)])
    return ''.join(output)

def convert_to_string(data):
    '''Muuttaa tavuina annetun datan binääriseksi merkkijonoksi'''
    bin_data = []
    for item in data:
        bin_data.append(bin(int(item))[2:].zfill(8))

    return ''.join(bin_data)
