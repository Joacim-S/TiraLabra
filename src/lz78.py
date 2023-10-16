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
    output_byte_list = []
    for i in range(0, output_len, 8):
        output_byte_list.append(int(output_string[i:i+8], 2))
    
    result = bytearray(output_byte_list)

    return result