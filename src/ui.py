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
                    ('compress_and_decompress', 'pakkaa ja purkaa tiedoston'),
                    ('exit', 'sulkee ohjelman')]
    file_prompt = 'tiedosto:'
    algo_prompt = 'algoritmi ("lz" tai "h", "" = molemmat):'

    while True:
        command = input()
        if command == 'help':
            for item in command_help:
                print(f'{item[0]:30} - {item[1]}')

        elif command in ('list_input', 'list_compressed', 'list_decompressed'):
            files = commands.handle_list(command[5:])
            if not files:
                print('tyhjä kansio')
            for file in files:
                print(file)

        elif command in ('compress', 'decompress'):
            try:
                file = input(file_prompt)
                if command == 'compress':
                    commands.file_exists(f'input/{file}')
                    result = commands.handle_compress(file, input(algo_prompt))

                elif command == 'decompress':
                    commands.file_exists(f'output/compressed/{file}')
                    result = commands.handle_decompress(file)

                if result:
                    print(f'suoritettu ajassa: {result}')
                else:
                    print('jotain meni vikaan')
            except FileNotFoundError:
                print('Tiedostoa ei löytynyt')
        
        elif command == 'exit':
            break

        else:
            print('Virheellinen komento')
            print('Kirjoita "help" jos haluat listan komennoista')
