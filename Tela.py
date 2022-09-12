import os


def LimpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
