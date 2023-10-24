import commands

'''Sovelluksen käyttöliittymä'''
def start():
    '''
    Sovelluksen käyttöliittymä
    '''
    print('Kirjoita "help" jos haluat listan komennoista')
    command_help = [('list_input', 'lisktaa input kansion tiedostot'),
                    ('list_compressed', 'listaa pakatut tiedostot'),
                    ('list_decompressed', 'listaa puretut tiedostot'),
                    ('compress', 'pakkaa tiedoston'),
                    ('decompress', 'purkaa tiedoston'),
                    ('compress_and_decompress', 'pakkaa ja purkaa tiedoston')]
    file_prompt = 'tiedosto:'
    while True:
        command = input()
        if command == 'help':
            for item in command_help:
                print(f'{item[0]:30} - {item[1]}')

        elif command == 'compress':
            try:
                commands.handle_compress(input(file_prompt))
            except FileNotFoundError:
                print('Tiedostoa ei löytynyt')

        elif command in ('list_input', 'list_compressed', 'list_decompressed'):
            files = commands.handle_list(command[5:])
            if not files:
                print('tyhjä kansio')
            for file in files:
                print(file)

        else:
            print('Virheellinen komento')
            print('Kirjoita "help" jos haluat listan komennoista')
        