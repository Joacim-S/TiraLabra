'''LZ78 algoritmilla pakkaus ja myöhemmin purku'''
def compress(text=str):
    '''Koodaa syötetyn merkkijonon LZ78 algoritmilla ja palauttaa koodatun jonon,
    jossa mukana EOF merkkinä toimiva "$"'''
    text += '$'
    output = ''
    dictionary = [(0,'')]
    last_match = 0
    i = 0
    while i < len(text):
        for j, item in enumerate(dictionary):
            print(j)
            if item == (last_match, text[i]):
                last_match = j
                i += 1
        dictionary.append((last_match, text[i]))
        output += f'{last_match}{text[i]}'
        last_match = 0
        i+=1
    return output