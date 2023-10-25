def to_bytes(data=list):
    '''Muuttaa listana olevan datan kokonaisiksi tavuiksi'''
    output_string = ''.join(data)
    to_next_byte = 8 - len(output_string) % 8
    output_string_prefixed = f'{"0"*(to_next_byte-1)}1{output_string}'
    output_byte_list = []

    for i in range(0, len(output_string_prefixed), 8):
        output_byte_list.append(int(output_string_prefixed[i:i+8], 2))

    return bytearray(output_byte_list)

def to_string(data):
    '''Muuttaa tavuina annetun datan binääriseksi merkkijonoksi'''
    bin_data = []
    for item in data:
        bin_data.append(bin(int(item))[2:].zfill(8))

    return ''.join(bin_data)

def get_start_of_data(data_string):
    i = 0
    while data_string[i] == '0':
        i += 1
    i += 1
    return i

def get_char_length(bits):
    chr_bits = 8
    for bit in bits:
        if bit == '0':
            break
        chr_bits += 8

    if chr_bits > 8:
        chr_bits -= 8
        
    return chr_bits