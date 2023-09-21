def compress(text=str):
    text += '$'
    output = ''
    dictionary = [(0,'')]
    last_match = 0
    i = 0
    while i < len(text):
        for j in range(len(dictionary)):
            if dictionary[j] == (last_match, text[i]):
                last_match = j
                i += 1
        dictionary.append((last_match, text[i]))
        output += f'{last_match}{text[i]}'
        last_match = 0
        i+=1

    return output

