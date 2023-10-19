'''LZ78 algoritmilla pakkaus ja myöhemmin purku'''
def compress(text):
    '''Koodaa syötetyn merkkijonon LZ78 algoritmilla'''
    last_match = 0
    next_index = 2
    i = 1
    dictionary = {(0, '') : 0, (0, text[0]) : 1}
    output = [bin(ord(text[0]))[2:].zfill(8)]
    bits = 1
    rounds = 0
    round_limit = 1
    added = False
    print('Luodaan sanakirjaa...')
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
            output.append(f'{last_match:0{bits}b}{bin(ord(text[i]))[2:].zfill(8)}')
            last_match = 0
            i+=1
            rounds += 1
            if rounds == round_limit:
                bits += 1
                round_limit *= 2
                rounds = 0
    if not added:
        output.append(f'{last_match:0{bits}b}')

    print('Muutetaan tavuiksi...')
    output_string = ''.join(output)
    output_len = len(output_string)
    to_next_byte = 8 - output_len % 8
    output_string_prefixed = f'{"0"*(to_next_byte-1)}1{output_string}'
    output_byte_list = []
    print(len(output_string_prefixed)/8)
    for i in range(0, len(output_string_prefixed), 8):
        output_byte_list.append(int(output_string_prefixed[i:i+8], 2))
    
    result = bytearray(output_byte_list)

    return result

def decompress(data):
    output = []
    bits = 0
    rounds = 0
    round_limit = 0.5
    bin_data = []
    print('Luetaan dataa...')
    for item in data:
        bin_data.append(bin(int(item))[2:].zfill(8))
    
    compressed = ''.join(bin_data)
    dictionary = {0 : ''}
    i = 0
    next_index = 1

    while compressed[i] == '0':
        i += 1
    i += 1

    print('Puretaan...')
    while i < len(compressed)-bits and i < len(compressed) - 8:
        previous = ''
        if bits:
            key = int(compressed[i:i+bits], 2)
            i += bits
            previous = dictionary[key]
        chr_bits = 8

        for bit in compressed[i:]:
            if bit == '0':
                break
            chr_bits += 8

        if chr_bits > 8:
            chr_bits -= 8
        
        next_char = chr(int(compressed[i:i+chr_bits], 2))
        segment = f'{previous}{next_char}'
        output.append(segment)
        dictionary[next_index] = segment
        next_index += 1
        i += chr_bits

        rounds += 1
        if rounds >= round_limit:
            bits += 1
            round_limit *= 2
            rounds = 0
    print(segment)
    print('Yhdistetään merkkijonoksi...')
    if i < len(compressed):
        print(dictionary[int(compressed[i:], 2)])
        output.append(dictionary[int(compressed[i:], 2)])

    output_string = ''.join(output)
    return output_string
