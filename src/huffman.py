import heapq

def compress(text=str):
    frequencies = get_frequencies(text)
    heap = get_heap(frequencies)
    return(heap)

def get_frequencies(text=str):
    frequencies = {}
    for char in text:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1

    return frequencies

def get_heap(frequencies):
    f_list = []
    for char, freq in frequencies.items():
        f_list.append((freq, char))
    heapq.heapify(f_list)

    return f_list

print(compress('Tämä on testiteksti jolla testaan toimiiko kaikki ollenkaan ja ehkä oiekinkin.'))