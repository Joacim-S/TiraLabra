'''Sovelluksen käyttöliittymä'''
import commands


def start():
    '''
    Sovelluksen käyttöliittymä
    '''
    print('Kirjoita "help" jos haluat listan komennoista')
    command_help = [('list_input', 'lisktaa input kansion tiedostot'),
                    ('list_compressed', 'listaa pakatut tiedostot'),
                    ('list_decompressed', 'listaa puretut tiedostot'),
                    ('compress', 'pakkaa tiedoston'),
                    ('compress_stats', 'Pakkaa tiedostot ja tallentaa tilastot'),
                    ('decompress', 'purkaa tiedoston'),
                    ('exit', 'sulkee ohjelman')]
    file_prompt = 'tiedosto ("" = kaikki):'
    algo_prompt = 'algoritmi ("lz" tai "h", "" = molemmat):'

    while True:
        command = input()

        if command == 'exit':
            break

        if command == 'help':
            for item in command_help:
                print(f'{item[0]:30} - {item[1]}')

        elif command in ('list_input', 'list_compressed', 'list_decompressed'):
            files = commands.handle_list(command[5:])
            if not files:
                print('tyhjä kansio')
            for file in files:
                print(file)

        elif command == 'compress_stats':
            print(f'suoritettu ajassa: {commands.handle_compress_stats()}')

        elif command in ('compress', 'decompress'):
            file = input(file_prompt)

            if file:
                try:
                    commands.file_exists(file, command)
                except FileNotFoundError:
                    print('Tiedostoa ei löytynyt')
                    continue
                if command == 'compress':
                    result = commands.handle_compress(
                        file, input(algo_prompt))[0]
                    print(f'suoritettu ajassa: {result}')
                    continue

            if command == 'decompress':
                result = commands.handle_decompress(file)
            else:
                result = commands.handle_compress(file, input(algo_prompt))

            print(f'suoritettu ajassa: {result}')

        else:
            print('Virheellinen komento')
            print('Kirjoita "help" jos haluat listan komennoista')
