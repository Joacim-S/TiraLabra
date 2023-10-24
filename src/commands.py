import os

def handle_compress(file):
    files = os.listdir('test_files')
    if file not in files:
        raise FileNotFoundError

def handle_list(dir):
    if dir == 'input':
        return os.listdir(dir)
    return os.listdir(f'output/{dir}')