'''LZ78 algoritmilla pakkaus ja myöhemmin purku'''
def compress_too_slow(text=str):
    '''Koodaa syötetyn merkkijonon LZ78 algoritmilla ja palauttaa koodatun jonon,
    jossa mukana EOF merkkinä toimiva "$"'''
    text += '$'
    output = ''
    dictionary = [(0,'')]
    last_match = 0
    i = 0
    while i < len(text):
        for j, item in enumerate(dictionary):
            if item == (last_match, text[i]):
                last_match = j
                i += 1
        dictionary.append((last_match, text[i]))
        output += f'{last_match}{text[i]}'
        last_match = 0
        i+=1
    return output

def compress(text=str):
    '''Koodaa syötetyn merkkijonon LZ78 algoritmilla ja palauttaa koodatun jonon,
    jossa mukana EOF merkkinä toimiva "$"'''
    text += '$'
    output = ''
    dictionary = {(0, '') : 0}
    last_match = 0
    next_index = 1
    i = 0
    while i < len(text):
        key = (last_match, text[i])
        if key in dictionary:
            last_match = dictionary[key]
            i += 1

        else:
            dictionary[last_match, text[i]] = next_index
            next_index += 1
            output += f'{last_match}{text[i]}'
            last_match = 0
            i+=1
    return output