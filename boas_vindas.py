import menu_nav
import os

def vindas( ):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('Seja bem vindo ao Organico’s 🙂.\nAqui você pode comprar nossos produtos direto pelo seu celular!')
    red = (int(input('Digite o número de uma das opções abaixo: \n 1 - Menu de Navegação \n 2 - Encerrar o programa. \n')))
    if red == 1:
        print('Que bom que está continuando com a gente! Você está sendo redirecionada (o) para o nosso menu de navegação!')
        menu_nav.nav()
    elif red == 2:
        print('Obrigada por visitar nosso programa. Volte sempre!')
vindas()