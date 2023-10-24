'''Käynnistää sovelluksen'''
import ui
import filecmp

def main():
    ui.start()

def lz78_decompress():
    start = datetime.now()
    with open('output.bin', 'rb') as file:
        data = file.read()

    decompressed = lz78.decompress(data)

    with open('decompressed.txt', 'w') as file:
        file.write(decompressed)

    print(datetime.now()-start)
    print(filecmp.cmp('input.txt', 'decompressed.txt', False))

if __name__ == '__main__':
    main()
